class InvalidBinaryInputError(ValueError):
    def __init__(self, value: str):
        super().__init__(f"'{value}' is not a valid binary string")

class NegativeBinaryResultError(ValueError):
    def __init__(self):
        super().__init__("Binary subtraction result cannot be negative")