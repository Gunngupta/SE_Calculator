from .exceptions import InvalidBinaryInputError, NegativeBinaryResultError


def _strip(b: str) -> str:
    """Strip B' prefix and whitespace."""
    b = b.strip().upper()
    if b.startswith("B'"):
        b = b[2:]
    return b


def _validate(b: str) -> None:
    if not b or not all(c in '01' for c in b):
        raise InvalidBinaryInputError(b)
    

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