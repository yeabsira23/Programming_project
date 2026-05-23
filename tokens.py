# tokens.py

from enum import Enum, auto


class TokenType(Enum):

    # Keywords
    ASSIGN = auto()       # አድርግ
    PRINT = auto()        # አሳይ
    IF = auto()           # ከሆነ
    ELSE = auto()         # ካልሆነ
    WHILE = auto()        # እስከ
    FUNCTION = auto()     # ተግባር
    RETURN = auto()       # መልስ
    END = auto()          # ጨርስ

    # Identifiers and literals
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()

    EQUAL = auto()
    EQUAL_EQUAL = auto()

    LESS = auto()
    GREATER = auto()

    # Symbols
    LPAREN = auto()
    RPAREN = auto()
    COMMA = auto()

    # Structure
    NEWLINE = auto()
    EOF = auto()


class Token:

    def __init__(self, token_type, value=None):
        self.type = token_type
        self.value = value

    def __repr__(self):
        return f"{self.type.name}({self.value})"