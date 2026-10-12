
import ast
import operator

# Our calculator tool
def calculator(expression):
    allowed_operators = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
    }

    def calculate(node):
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in allowed_operators:
            left = calculate(node.left)
            right = calculate(node.right)
            return allowed_operators[type(node.op)](left, right)

        raise ValueError("Unsupported calculation")

    return calculate(ast.parse(expression, mode="eval").body)


# Test our tool
print("10 + 20 =", calculator("10 + 20"))
print("50 - 15 =", calculator("50 - 15"))
print("6 * 7 =", calculator("6 * 7"))
