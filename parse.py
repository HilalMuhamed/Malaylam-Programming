import sys
from lex import *

class Parser:
    
    def __init__(s, lexer,codeGen   ):
        s.lexer = lexer
        s.codeGen = codeGen
        
        s.symbols = set()
        s.labelsDeclared = set()
        s.labelsGotoed = set()
        
        s.curToken = None
        s.peekToken = None
        s.nextToken()
        s.nextToken()
    
    def checkToken(s,kind):
        return s.curToken.kind == kind
    
    def checkPeek(s,kind):
        return s.peekToken.kind == kind
    
    def match(s,kind):
        if not s.checkToken(kind):
            s.abort("Expected "+kind.name+", got "+s.curToken.kind.name)
        s.nextToken()
    
    def nextToken(s):
        s.curToken = s.peekToken
        s.peekToken = s.lexer.getToken()
    
    def abort(s,msg):
        sys.exit("Error . " + msg)
        
    
    #program ::= {statement}
    def program(s):
        s.codeGen.headerLine("#include<stdio.h>")
        s.codeGen.headerLine("int main(){")
        while s.checkToken(TokenType.NEWLINE):
            s.nextToken()
            
        while not s.checkToken(TokenType.EOF):
            s.statement()
        
        s.codeGen.genLine("return 0;")
        s.codeGen.genLine("}")
        
        for label in s.labelsGotoed:
            if label not in s.labelsDeclared:
                s.abort("Attempting to goto undeclared label : "+label)
    
    
    #statement ::= "PRINT" (expression | string) nl
    def statement(s):
        
        # "PRINT" (expression | string)
        if s.checkToken(TokenType.PRINT):
            print("Statement-Print")
            s.nextToken()
            
            if s.checkToken(TokenType.STRING):
                s.codeGen.genLine("printf(\""+s.curToken.text+"\\n\");")
                # String
                s.nextToken()
            else:
                # Expression
                s.codeGen.gen("printf(\"%" + ".2f\\n\", (float)(")
                s.expression()
                s.codeGen.genLine("));")
        # "IF" comparison "THEN" {statement} "ENDIF"
        elif s.checkToken(TokenType.IF):
            print("Statement-IF")
            s.nextToken()
            s.codeGen.gen("if(")
            s.comparison()
            s.match(TokenType.LBRACE)
            while s.checkToken(TokenType.NEWLINE):
                s.nextToken()
            s.codeGen.genLine("){")
            while not s.checkToken(TokenType.RBRACE):
                s.statement()
            s.match(TokenType.RBRACE)
            while s.checkToken(TokenType.NEWLINE):
                s.nextToken()
            if s.checkToken(TokenType.ELSE):
                s.codeGen.genLine("} else {")
                s.nextToken()
                s.match(TokenType.LBRACE)
                while s.checkToken(TokenType.NEWLINE):
                    s.nextToken()
                while not s.checkToken(TokenType.RBRACE):
                    s.statement()
                s.match(TokenType.RBRACE)
            s.codeGen.genLine("}")
        # "WHILE" comparison "REPEAT" {statement} "ENDWHILE"
        
        elif s.checkToken(TokenType.WHILE):
            print("Statement-While")
            s.nextToken()
            s.codeGen.gen("while(")
            s.comparison()
            s.match(TokenType.LBRACE)
            while s.checkToken(TokenType.NEWLINE):
                s.nextToken()
            s.codeGen.genLine("){")
            while not s.checkToken(TokenType.RBRACE):
                s.statement()
            s.match(TokenType.RBRACE)
            s.codeGen.genLine("}")
        
        
        # "LET" ident "=" expression
        elif (s.checkToken(TokenType.INT) or 
                s.checkToken(TokenType.FLOAT) or 
                s.checkToken(TokenType.BOOL) or 
                s.checkToken(TokenType.STR)):
            print("Statement-Declaration")
            varType = s.curToken.kind
            s.nextToken()
            
            if s.curToken.text not in s.symbols:
                s.symbols.add(s.curToken.text)
                cType = {
                    TokenType.INT: "int",
                    TokenType.FLOAT: "float",
                    TokenType.BOOL: "int",
                    TokenType.STR: "char[256]"
                }[varType]
                s.codeGen.headerLine(cType + " " + s.curToken.text+";")
                
            s.codeGen.gen( s.curToken.text+" = ")
            s.match(TokenType.IDENT)
            s.match(TokenType.EQ)
            s.expression()
            s.codeGen.genLine(";")

        # "INPUT" ident
        elif s.checkToken(TokenType.INPUT):
            print("Statement-Input")
            s.nextToken()
            
            if s.curToken.text not in s.symbols:
                s.symbols.add(s.curToken.text)
                s.codeGen.headerLine("float " + s.curToken.text+";")
            s.codeGen.genLine("if(0 == scanf(\"%" + "f\", &" + s.curToken.text + ")) {")
            s.codeGen.genLine(s.curToken.text + " = 0;")
            s.codeGen.gen("scanf(\"%")
            s.codeGen.genLine("*s\");")
            s.codeGen.genLine("}")
            s.match(TokenType.IDENT)
        else:
            s.abort("Invalid statement at "+s.curToken.text+"("+s.curToken.kind.name+")")
        # New Line
        s.nl()
    
    # nl ::= '\n'+
    def nl(s):
        
        print("New Line ")
        s.match(TokenType.NEWLINE)
        while s.checkToken(TokenType.NEWLINE):
            s.nextToken()
    
    # comparison ::= expression (("==" | "!=" | ">" | ">=" | "<" | "<=") expression)+
    def comparison(s):
        print("Comparison")
        s.expression()
        
        if s.isComparisonOperator():
            s.codeGen.gen(s.curToken.text)
            s.nextToken()
            s.expression()
        else:
            s.abort("Expected comparitor operator at " + s.curToken.text)
        
        while s.isComparisonOperator():
            s.codeGen.gen(s.curToken.text)
            s.nextToken()
            s.expression()
    
    def isComparisonOperator(s):
        return (s.checkToken(TokenType.GT)
                or s.checkToken(TokenType.GTEQ) 
                or s.checkToken(TokenType.LT)
                or s.checkToken(TokenType.LTEQ) 
                or s.checkToken(TokenType.EQEQ) 
                or s.checkToken(TokenType.NOTEQ))

    # expression ::= term {( "-" | "+" ) term}
    def expression(s):
        print("Expression")
        s.term()
        
        while s.checkToken(TokenType.PLUS) or s.checkToken(TokenType.MINUS):
            s.codeGen.gen(s.curToken.text)
            s.nextToken()
            s.term()
    
    # term ::= unary {( "/" | "*" ) unary}
    def term(s):
        print("Term")
        s.unary()
        while s.checkToken(TokenType.SLASH) or s.checkToken(TokenType.ASTERISK):
            s.codeGen.gen(s.curToken.text)
            s.nextToken()
            s.unary()
            
    # unary ::= ["+" | "-"] primary
    def unary(s):
        print("Unary")
        if s.checkToken(TokenType.PLUS) or s.checkToken(TokenType.MINUS):
            s.codeGen.gen(s.curToken.text)
            s.nextToken()
        s.primary()
        
    # primary ::= number | ident        
    def primary(s):
        print("Primary (" +s.curToken.text +")")
        if s.checkToken(TokenType.NUMBER):
            s.codeGen.gen(s.curToken.text)
            s.nextToken()
        elif s.checkToken(TokenType.IDENT):
            if s.curToken.text not in s.symbols:
                s.abort("Variable is not declared yet : "+s.curToken.text)
            s.codeGen.gen(s.curToken.text)
            s.nextToken()
        else:
            s.abort("Unexpected token at "+s.curToken.text)
    