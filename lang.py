from lex import *
from codeGen import *
from parse import *
from mal_to_manglish import convert_file
import sys
import time

def main():
    start = time.time()
    print("Malayalam Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")

    input_file = sys.argv[1]
    converted_file = "converted_temp.malang"

    convert_file(input_file, converted_file)

    with open(converted_file, 'r', encoding='utf-8') as inputFile:
        source = inputFile.read()

    lexer = Lexer(source)
    codeGen = CodeGen("out.c")
    parser = Parser(lexer, codeGen)

    parser.program()
    codeGen.writeFile()

    end = time.time()
    print(f"Compilation finished in {end - start:.4f} seconds")

main()
