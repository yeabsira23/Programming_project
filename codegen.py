from ast_nodes import *


class CodeGenerator:

    def __init__(self):

        self.output = []
        self.indent_level = 0

    # ---------------------------------------------------
    # Indentation
    # ---------------------------------------------------

    def indent(self):

        return "    " * self.indent_level

    # ---------------------------------------------------
    # Generate code
    # ---------------------------------------------------

    def generate(self, node):

        method_name = f"generate_{type(node).__name__}"

        method = getattr(self, method_name)

        return method(node)

    # ---------------------------------------------------
    # Program
    # ---------------------------------------------------

    def generate_ProgramNode(self, node):

        for statement in node.statements:
            self.generate(statement)

        return "\n".join(self.output)

    # ---------------------------------------------------
    # Assignment
    # ---------------------------------------------------

    def generate_AssignmentNode(self, node):

        value = self.generate(node.value)

        line = f"{self.indent()}{node.variable_name} = {value}"

        self.output.append(line)

    # ---------------------------------------------------
    # Print
    # ---------------------------------------------------

    def generate_PrintNode(self, node):

        value = self.generate(node.value)

        line = f"{self.indent()}print({value})"

        self.output.append(line)

    # ---------------------------------------------------
    # Numbers
    # ---------------------------------------------------

    def generate_NumberNode(self, node):

        return str(node.value)

    # ---------------------------------------------------
    # Variables
    # ---------------------------------------------------

    def generate_VariableNode(self, node):

        return node.name

    # ---------------------------------------------------
    # Binary Operations
    # ---------------------------------------------------

    def generate_BinaryOperationNode(self, node):

        left = self.generate(node.left)

        right = self.generate(node.right)

        operator = node.operator.value

        return f"{left} {operator} {right}"

    # ---------------------------------------------------
    # If Statement
    # ---------------------------------------------------

    def generate_IfNode(self, node):

        condition = self.generate(node.condition)

        self.output.append(
            f"{self.indent()}if {condition}:"
        )

        self.indent_level += 1

        for statement in node.body:
            self.generate(statement)

        self.indent_level -= 1

        # Else block
        if node.else_body:

            self.output.append(
                f"{self.indent()}else:"
            )

            self.indent_level += 1

            for statement in node.else_body:
                self.generate(statement)

            self.indent_level -= 1

    # ---------------------------------------------------
    # While Loop
    # ---------------------------------------------------

    def generate_WhileNode(self, node):

        condition = self.generate(node.condition)

        self.output.append(
            f"{self.indent()}while {condition}:"
        )

        self.indent_level += 1

        for statement in node.body:
            self.generate(statement)

        self.indent_level -= 1

    # ---------------------------------------------------
    # Function Definition
    # ---------------------------------------------------

    def generate_FunctionNode(self, node):

        parameters = ", ".join(node.parameters)

        self.output.append(
            f"{self.indent()}def {node.name}({parameters}):"
        )

        self.indent_level += 1

        for statement in node.body:
            self.generate(statement)

        self.indent_level -= 1

    # ---------------------------------------------------
    # Return Statement
    # ---------------------------------------------------

    def generate_ReturnNode(self, node):

        value = self.generate(node.value)

        self.output.append(
            f"{self.indent()}return {value}"
        )

    # ---------------------------------------------------
    # Function Call
    # ---------------------------------------------------

    def generate_FunctionCallNode(self, node):

        arguments = []

        for arg in node.arguments:
            arguments.append(self.generate(arg))

        args_text = ", ".join(arguments)

        return f"{node.name}({args_text})"