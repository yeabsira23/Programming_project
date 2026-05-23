from lexer import Lexer
from parser import Parser

source_code = """
አድርግ x = 5
አሳይ x
"""

lexer = Lexer(source_code)

tokens = lexer.get_tokens()

parser = Parser(tokens)

ast = parser.parse()

print(ast)