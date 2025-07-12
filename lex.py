import enum
import sys

class Lexer:
    
    def __init__(s,source):
        s.source = source + '\n'
        s.curChar = ""
        s.curPos = -1
        s.nextChar()
    
    def nextChar(s):
        s.curPos +=1
        if s.curPos >= len(s.source):
            s.curChar = "\0" # EOF
        else:
            s.curChar = s.source[s.curPos]
    
    def peek(s):
        if s.curPos + 1 >= len(s.source):
            return "\0"
        else:
            return s.source[s.curPos+1]
    
    def abort(s,msg):
        sys.exit("Lexing error. " + msg)
    
    def skipWhiteSpaces(s):
        while s.curChar == " " or s.curChar =="\t"  or s.curChar == "\r":
            s.nextChar()
    
    def skipComment(s):
        
        if s.curChar == "#":
            while s.curChar != "\n":
                s.nextChar()
    
    def getToken(s):
        
        s.skipWhiteSpaces()
        s.skipComment()
        token = None
        if s.curChar =='+':
            token = Token(s.curChar,TokenType.PLUS)
        elif s.curChar =='-':
            token = Token(s.curChar, TokenType.MINUS)
        elif s.curChar =='*':
            token = Token(s.curChar, TokenType.ASTERISK)
        elif s.curChar =='/':
            token = Token(s.curChar, TokenType.SLASH)
        elif s.curChar =='\n':
            token = Token(s.curChar, TokenType.NEWLINE)
        elif s.curChar =='\0':
            token = Token("", TokenType.EOF)
        elif s.curChar == '=':
            if s.peek() == '=':
                lastChar = s.curChar
                s.nextChar()
                token = Token(lastChar+s.curChar,TokenType.EQEQ)
            else:
                token = Token(s.curChar,TokenType.EQ)
        elif s.curChar == '>':
            if s.peek() == '=':
                lastChar = s.curChar
                s.nextChar()
                token = Token(lastChar+s.curChar,TokenType.GTEQ)
            else:
                token = Token(s.curChar,TokenType.GT)
        elif s.curChar == '<':
            if s.peek() == '=':
                lastChar = s.curChar
                s.nextChar()
                token = Token(lastChar+s.curChar,TokenType.LTEQ)
            else:
                token = Token(s.curChar,TokenType.LT)
        elif s.curChar == '!':
            if s.peek() == '=':
                lastChar = s.curChar
                s.nextChar()
                token = Token(lastChar+s.curChar,TokenType.NOTEQ)
            else:
                s.abort("Got ! but should !=" + s.peek())
        elif s.curChar == "\"":
            s.nextChar()
            startPos = s.curPos
            while s.curChar !="\"":
                if s.curChar == '\r' or s.curChar == '\n' or s.curChar == '\t' or s.curChar == '\\' or s.curChar == '%':
                    s.abort("Illegal character in String . ")
                s.nextChar()
            tokenText = s.source[startPos:s.curPos]
            token=Token(tokenText,TokenType.STRING)
        elif s.curChar == '{':
            token = Token(s.curChar, TokenType.LBRACE)
        elif s.curChar == '}':
            token = Token(s.curChar, TokenType.RBRACE)
        elif s.curChar.isdigit():
            startPos = s.curPos
            while s.peek().isdigit():
                s.nextChar()
            if s.peek() == ".":
                s.nextChar()
                if not s.peek().isdigit():
                    s.abort("Illegal character in number ")
                while s.peek().isdigit():
                    s.nextChar()
            tokenText = s.source[startPos:s.curPos +1]
            token=Token(tokenText,TokenType.NUMBER)
        elif s.curChar.isalpha() :
            startPos=s.curPos
            while s.peek().isalnum():
                s.nextChar()
            tokenText = s.source[startPos:s.curPos+1]
            keyword = Token.checkIfKeyword(tokenText)
            if  keyword == None:
                token = Token(tokenText,TokenType.IDENT)
            else:
                token = Token(tokenText,keyword)
        else:
            s.abort("Unknown token: " + s.curChar)
        s.nextChar()
        return token


class Token:
    def __init__(s,tokenText,tokenKind):
        s.text = tokenText
        s.kind = tokenKind
    @staticmethod
    def checkIfKeyword(tokenText):
        return keyword_map.get(tokenText)
    

class TokenType(enum.Enum):
    EOF = -1
    NEWLINE = 0
    NUMBER = 1
    IDENT = 2
    STRING = 3 

    # Keywords (100-199)
    PRINT = 103
    INPUT = 104
    IF = 107
    WHILE = 108
    INT = 109
    FLOAT = 110
    BOOL = 111
    STR = 112
    ELSE = 114
    
    # Operators (200+)
    EQ = 201
    PLUS = 202
    MINUS = 203
    ASTERISK = 204
    SLASH = 205
    EQEQ = 206
    NOTEQ = 207
    LT = 208
    LTEQ = 209
    GT = 210
    GTEQ = 211
    LBRACE = 212
    RBRACE = 213
keyword_map = {
    # PRINT
    "PRINT": TokenType.PRINT,
    "എഴുതി": TokenType.PRINT,
    "ezhuthi": TokenType.PRINT,
    
    # INPUT
    "INPUT": TokenType.INPUT,
    "വായിക്കുക": TokenType.INPUT,
    "vaayikkuka": TokenType.INPUT,
    "വായിക": TokenType.INPUT,
    "vaayika": TokenType.INPUT,

    # IF
    "IF": TokenType.IF,
    "സത്യമെങ്കിൽ": TokenType.IF,
    "sathyamenkil": TokenType.IF,

    #ELSE
    
    "ELSE": TokenType.ELSE,
    "കലമെങ്കിൽ": TokenType.ELSE,
    "kalamenkil": TokenType.ELSE,

    # WHILE
    "WHILE": TokenType.WHILE,
    "എത്രകാലം": TokenType.WHILE,
    "ethrakaalam": TokenType.WHILE,


    # INT
    "INT": TokenType.INT,
    "പൂർണ്ണസംഖ്യ": TokenType.INT,
    "poornnasankhya": TokenType.INT,

    # FLOAT
    "FLOAT": TokenType.FLOAT,
    "ദശാംശം": TokenType.FLOAT,
    "dashamsham": TokenType.FLOAT,

    # BOOL
    "BOOL": TokenType.BOOL,
    "സത്യമായ": TokenType.BOOL,
    "sathyamaaya": TokenType.BOOL,
    "സത്യം": TokenType.BOOL,
    "sathyam": TokenType.BOOL,

    # STRING
    "STR": TokenType.STR,
    "വാചകം": TokenType.STR,
    "vaachakam": TokenType.STR,
    
    
}
