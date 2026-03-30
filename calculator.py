import re
from modules.binary import (
    binary_to_decimal, decimal_to_binary,
    binary_add, binary_subtract,
    binary_multiply, binary_divide,
    ones_complement, twos_complement,
)


class Calculator:
    def add(self, a, b):        return a + b
    def subtract(self, a, b):   return a - b
    def multiply(self, a, b):   return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero")
        return a / b

    def evaluate(self, expression: str) -> str:
        """
        Route string expressions to the correct module.
        Examples:
            "bin(10)"          -> "B'1010"
            "dec(B'1010)"      -> "D'10"
            "1s(B'1010)"       -> "B'0101"
            "2s(B'0111)"       -> "B'1001"
            "B'011 + B'010"    -> "B'101"
        """
        expr = expression.strip()

        if re.match(r"^bin\(", expr, re.I):
            val = re.search(r"\((.+)\)", expr).group(1).strip()
            return decimal_to_binary(f"D'{val}'" if not val.upper().startswith("D'") else val)

        if re.match(r"^dec\(", expr, re.I):
            val = re.search(r"\((.+)\)", expr).group(1).strip()
            return binary_to_decimal(val)

        if re.match(r"^1s\(", expr, re.I):
            val = re.search(r"\((.+)\)", expr).group(1).strip()
            return ones_complement(val)

        if re.match(r"^2s\(", expr, re.I):
            val = re.search(r"\((.+)\)", expr).group(1).strip()
            return twos_complement(val)

        # Binary arithmetic: "B'011 + B'010"
        m = re.match(
            r"(B'[01]+)\s*([\+\-\\/])\s(B'[01]+)", expr, re.I
        )
        if m:
            a, op, b = m.group(1), m.group(2), m.group(3)
            ops = {'+': binary_add, '-': binary_subtract,
                   '*': binary_multiply, '/': binary_divide}
            return ops[op](a, b)

        raise ValueError(f"Unrecognised expression: {expression}")