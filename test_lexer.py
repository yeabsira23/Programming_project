from lexer import Lexer

source_code = """
አድርግ x = 5
አሳይ x
"""

lexer = Lexer(source_code)

tokens = lexer.get_tokens()

for token in tokens:
    print(token)