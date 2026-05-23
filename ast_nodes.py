# ast_nodes.py

# -----------------------------------------
# Base Node
# -----------------------------------------

class ASTNode:
    pass


# -----------------------------------------
# Program Node
# -----------------------------------------

class ProgramNode(ASTNode):

    def __init__(self, statements):
        self.statements = statements


# -----------------------------------------
# Variable Assignment
# -----------------------------------------

class AssignmentNode(ASTNode):

    def __init__(self, variable_name, value):
        self.variable_name = variable_name
        self.value = value


# -----------------------------------------
# Print Statement
# -----------------------------------------

class PrintNode(ASTNode):

    def __init__(self, value):
        self.value = value


# -----------------------------------------
# Number Literal
# -----------------------------------------

class NumberNode(ASTNode):

    def __init__(self, value):
        self.value = value


# -----------------------------------------
# Variable Access
# -----------------------------------------

class VariableNode(ASTNode):

    def __init__(self, name):
        self.name = name


# -----------------------------------------
# Binary Operations
# -----------------------------------------

class BinaryOperationNode(ASTNode):

    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


# -----------------------------------------
# If Statement
# -----------------------------------------

class IfNode(ASTNode):

    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body


# -----------------------------------------
# While Loop
# -----------------------------------------

class WhileNode(ASTNode):

    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


# -----------------------------------------
# Function Definition
# -----------------------------------------

class FunctionNode(ASTNode):

    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body


# -----------------------------------------
# Function Call
# -----------------------------------------

class FunctionCallNode(ASTNode):

    def __init__(self, name, arguments):
        self.name = name
        self.arguments = arguments


# -----------------------------------------
# Return Statement
# -----------------------------------------

class ReturnNode(ASTNode):

    def __init__(self, value):
        self.value = value