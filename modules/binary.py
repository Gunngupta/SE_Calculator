from .exceptions import InvalidBinaryInputError, NegativeBinaryResultError


def _strip(b: str) -> str:
    """Strip B' prefix and whitespace."""
    b = b.strip().upper()
    if b.startswith("B'"):
        b = b[2:]
    return b


def _validate(b: str) -> None:
    if not b or not all(c in '0gi1' for c in b):
        raise InvalidBinaryInputError(b)
    


# Tanisha Gupta - Binary Arithmetic
def binary_add(a: str, b: str) -> str:
   
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    return decimal_to_binary(f"D'{da + db}")


def binary_subtract(a: str, b: str) -> str:
   
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    if da < db:
        raise NegativeBinaryResultError()
    bit_len = max(len(_strip(a)), len(_strip(b)))
    result = bin(da - db)[2:].zfill(bit_len)
    return f"B'{result}"


def binary_multiply(a: str, b: str) -> str:
   
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    return decimal_to_binary(f"D'{da * db}")


def binary_divide(a: str, b: str) -> str:
   
    da = int(binary_to_decimal(a).split("'")[1])
    db = int(binary_to_decimal(b).split("'")[1])
    if db == 0:
        raise ValueError("Binary division by zero")
    return decimal_to_binary(f"D'{da // db}")

#-----------Gunn 091: complement-------------------------------


def ones_complement(b: str) -> str:
    """
    Flip all bits.
    e.g. ones_complement("B'1010") -> "B'0101"
    """
    raw = _strip(b)
    _validate(raw)
    return "B'" + ''.join('1' if bit == '0' else '0' for bit in raw)


def twos_complement(b: str) -> str:
    """
    Add 1 to the one's complement.
    e.g. twos_complement("B'0111") -> "B'1001"
    """
    raw = _strip(b)
    _validate(raw)
    ones = ones_complement(f"B'{raw}")[2:]
    val = int(ones, 2) + 1                         # no modulo
    result = bin(val)[2:].zfill(len(ones))         # zfill won't truncate carry
    return f"B'{result}"