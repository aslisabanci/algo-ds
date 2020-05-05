HEXADECIMAL_DIGITS = "0123456789abcdef"


def convert_to_base(decimal_num: int, base: int) -> str:
    """Converts a decimal number to its representation in any base between 2 and 16.

    Arguments:
        decimal_num {int} -- Decimal number to convert
        base {int} -- Base to convert into

    Returns:
        str -- Converted number representation in the given base.
    """

    remainders = []
    while decimal_num > 0:
        remainder = decimal_num % base
        remainders.append(remainder)
        decimal_num = decimal_num // base

    result = []
    while remainders:
        result.append(HEXADECIMAL_DIGITS[remainders.pop()])
    return "".join(result)


# TODO: Move tests
print(convert_to_base(25, 8))
print(convert_to_base(25, 16))
print(convert_to_base(256, 16))
