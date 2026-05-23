# lexer.py

from tokens import TokenType, Token


class Lexer:

    KEYWORDS = {
        "አድርግ": TokenType.ASSIGN,
        "አሳይ": TokenType.PRINT,
        "ከሆነ": TokenType.IF,
        "ካልሆነ": TokenType.ELSE,
        "እስከ": TokenType.WHILE,
        "ተግባር": TokenType.FUNCTION,
        "መልስ": TokenType.RETURN,
        "ጨርስ": TokenType.END
    }

    def __init__(self, text):

        self.text = text
        self.position = 0
        self.current_char = self.text[self.position] if self.text else None

    # ---------------------------------------------------
    # Move to next character
    # ---------------------------------------------------

    def advance(self):

        self.position += 1

        if self.position >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.position]

    # ---------------------------------------------------
    # Skip spaces
    # ---------------------------------------------------

    def skip_whitespace(self):

        while self.current_char is not None and self.current_char in " \t":
            self.advance()

    # ---------------------------------------------------
    # Read numbers
    # ---------------------------------------------------

    def number(self):

        result = ""

        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return Token(TokenType.NUMBER, int(result))

    # ---------------------------------------------------
    # Read identifiers and keywords
    # ---------------------------------------------------

    def identifier(self):

        result = ""

        while (
            self.current_char is not None
            and (
                self.current_char.isalnum()
                or self.current_char == "_"
                or ord(self.current_char) > 127
            )
        ):
            result += self.current_char
            self.advance()

        token_type = self.KEYWORDS.get(result, TokenType.IDENTIFIER)

        return Token(token_type, result)

    # ---------------------------------------------------
    # Main tokenizer
    # ---------------------------------------------------

    def get_tokens(self):

        tokens = []

        while self.current_char is not None:

            # Skip spaces
            if self.current_char in " \t":
                self.skip_whitespace()
                continue

            # New lines
            if self.current_char == "\n":
                tokens.append(Token(TokenType.NEWLINE, "\\n"))
                self.advance()
                continue

            # Numbers
            if self.current_char.isdigit():
                tokens.append(self.number())
                continue

            # Identifiers / Keywords / Unicode
            if (
                self.current_char.isalpha()
                or self.current_char == "_"
                or ord(self.current_char) > 127
            ):
                tokens.append(self.identifier())
                continue

            # Operators
            if self.current_char == "+":
                tokens.append(Token(TokenType.PLUS, "+"))
                self.advance()
                continue

            if self.current_char == "-":
                tokens.append(Token(TokenType.MINUS, "-"))
                self.advance()
                continue

            if self.current_char == "*":
                tokens.append(Token(TokenType.MULTIPLY, "*"))
                self.advance()
                continue

            if self.current_char == "/":
                tokens.append(Token(TokenType.DIVIDE, "/"))
                self.advance()
                continue

            # Equals
            if self.current_char == "=":

                self.advance()

                if self.current_char == "=":
                    self.advance()
                    tokens.append(Token(TokenType.EQUAL_EQUAL, "=="))
                else:
                    tokens.append(Token(TokenType.EQUAL, "="))

                continue

            # Comparisons
            if self.current_char == "<":
                tokens.append(Token(TokenType.LESS, "<"))
                self.advance()
                continue

            if self.current_char == ">":
                tokens.append(Token(TokenType.GREATER, ">"))
                self.advance()
                continue

            # Parentheses
            if self.current_char == "(":
                tokens.append(Token(TokenType.LPAREN, "("))
                self.advance()
                continue

            if self.current_char == ")":
                tokens.append(Token(TokenType.RPAREN, ")"))
                self.advance()
                continue

            # Comma
            if self.current_char == ",":
                tokens.append(Token(TokenType.COMMA, ","))
                self.advance()
                continue

            # Unknown character
            raise Exception(f"Unknown character: {self.current_char}")

        tokens.append(Token(TokenType.EOF, None))

        return tokens