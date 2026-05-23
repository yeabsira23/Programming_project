from tokens import TokenType
from ast_nodes import *


class Parser:

    def __init__(self, tokens):

        self.tokens = tokens
        self.position = 0
        self.current_token = self.tokens[self.position]

    # ---------------------------------------------------
    # Advance token
    # ---------------------------------------------------

    def advance(self):

        self.position += 1

        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]

    # ---------------------------------------------------
    # Match expected token
    # ---------------------------------------------------

    def eat(self, token_type):

        if self.current_token.type == token_type:
            self.advance()
        else:
            raise Exception(
                f"Expected {token_type}, got {self.current_token.type}"
            )

    # ---------------------------------------------------
    # Parse whole program
    # ---------------------------------------------------

    def parse(self):

        statements = []

        while self.current_token.type != TokenType.EOF:

            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
                continue

            statement = self.statement()
            statements.append(statement)

        return ProgramNode(statements)

    # ---------------------------------------------------
    # Parse statements
    # ---------------------------------------------------

    def statement(self):

        token_type = self.current_token.type

        if token_type == TokenType.ASSIGN:
            return self.assignment_statement()

        elif token_type == TokenType.PRINT:
            return self.print_statement()

        elif token_type == TokenType.IF:
            return self.if_statement()

        elif token_type == TokenType.WHILE:
            return self.while_statement()

        elif token_type == TokenType.FUNCTION:
            return self.function_definition()

        elif token_type == TokenType.RETURN:
            return self.return_statement()

        else:
            raise Exception(
                f"Unexpected token: {self.current_token}"
            )

    # ---------------------------------------------------
    # Assignment
    # ---------------------------------------------------

    def assignment_statement(self):

        self.eat(TokenType.ASSIGN)

        variable_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)

        self.eat(TokenType.EQUAL)

        value = self.expression()

        return AssignmentNode(variable_name, value)

    # ---------------------------------------------------
    # Print
    # ---------------------------------------------------

    def print_statement(self):

        self.eat(TokenType.PRINT)

        value = self.expression()

        return PrintNode(value)

    # ---------------------------------------------------
    # If Statement
    # ---------------------------------------------------

    def if_statement(self):

        self.eat(TokenType.IF)

        condition = self.expression()

        body = []

        while (
            self.current_token.type != TokenType.ELSE
            and self.current_token.type != TokenType.END
        ):

            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
                continue

            body.append(self.statement())

        else_body = None

        if self.current_token.type == TokenType.ELSE:

            self.eat(TokenType.ELSE)

            else_body = []

            while self.current_token.type != TokenType.END:

                if self.current_token.type == TokenType.NEWLINE:
                    self.advance()
                    continue

                else_body.append(self.statement())

        self.eat(TokenType.END)

        return IfNode(condition, body, else_body)

    # ---------------------------------------------------
    # While Loop
    # ---------------------------------------------------

    def while_statement(self):

        self.eat(TokenType.WHILE)

        condition = self.expression()

        body = []

        while self.current_token.type != TokenType.END:

            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
                continue

            body.append(self.statement())

        self.eat(TokenType.END)

        return WhileNode(condition, body)

    # ---------------------------------------------------
    # Function Definition
    # ---------------------------------------------------

    def function_definition(self):

        self.eat(TokenType.FUNCTION)

        function_name = self.current_token.value
        self.eat(TokenType.IDENTIFIER)

        self.eat(TokenType.LPAREN)

        parameters = []

        while self.current_token.type != TokenType.RPAREN:

            parameters.append(self.current_token.value)

            self.eat(TokenType.IDENTIFIER)

            if self.current_token.type == TokenType.COMMA:
                self.eat(TokenType.COMMA)

        self.eat(TokenType.RPAREN)

        body = []

        while self.current_token.type != TokenType.END:

            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
                continue

            body.append(self.statement())

        self.eat(TokenType.END)

        return FunctionNode(function_name, parameters, body)

    # ---------------------------------------------------
    # Return Statement
    # ---------------------------------------------------

    def return_statement(self):

        self.eat(TokenType.RETURN)

        value = self.expression()

        return ReturnNode(value)

    # ---------------------------------------------------
    # Expressions
    # ---------------------------------------------------

    def expression(self):

        left = self.term()

        while self.current_token.type in (
            TokenType.PLUS,
            TokenType.MINUS,
            TokenType.LESS,
            TokenType.GREATER,
            TokenType.EQUAL_EQUAL
        ):

            operator = self.current_token

            self.advance()

            right = self.term()

            left = BinaryOperationNode(
                left,
                operator,
                right
            )

        return left

    # ---------------------------------------------------
    # Terms
    # ---------------------------------------------------

    def term(self):

        left = self.factor()

        while self.current_token.type in (
            TokenType.MULTIPLY,
            TokenType.DIVIDE
        ):

            operator = self.current_token

            self.advance()

            right = self.factor()

            left = BinaryOperationNode(
                left,
                operator,
                right
            )

        return left

    # ---------------------------------------------------
    # Factors
    # ---------------------------------------------------

    def factor(self):

        token = self.current_token

        # Numbers
        if token.type == TokenType.NUMBER:

            self.eat(TokenType.NUMBER)

            return NumberNode(token.value)

        # Variables
        elif token.type == TokenType.IDENTIFIER:

            name = token.value

            self.eat(TokenType.IDENTIFIER)

            # Function Call
            if self.current_token.type == TokenType.LPAREN:

                self.eat(TokenType.LPAREN)

                arguments = []

                while self.current_token.type != TokenType.RPAREN:

                    arguments.append(self.expression())

                    if self.current_token.type == TokenType.COMMA:
                        self.eat(TokenType.COMMA)

                self.eat(TokenType.RPAREN)

                return FunctionCallNode(name, arguments)

            return VariableNode(name)

        # Parentheses
        elif token.type == TokenType.LPAREN:

            self.eat(TokenType.LPAREN)

            expr = self.expression()

            self.eat(TokenType.RPAREN)

            return expr

        else:
            raise Exception(
                f"Unexpected token in expression: {token}"
            )