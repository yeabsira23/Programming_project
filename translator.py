import sys

from lexer import Lexer
from parser import Parser
from codegen import CodeGenerator


def translate_file(input_file):

    # Read source file
    with open(input_file, "r", encoding="utf-8") as file:
        source_code = file.read()

    # Lexer
    lexer = Lexer(source_code)
    tokens = lexer.get_tokens()

    # Parser
    parser = Parser(tokens)
    ast = parser.parse()

    # Code Generator
    generator = CodeGenerator()
    python_code = generator.generate(ast)

    # Output file
    output_file = input_file.replace(".yl", ".py")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(python_code)

    print(f"Translation successful!")
    print(f"Generated: {output_file}")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python translator.py program.yl")
    else:
        translate_file(sys.argv[1])