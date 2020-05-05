# TODO:
"""
Large integers are represented as list of digits. Sum them.
"""


def sum_two_str_ints(num1: str, num2: str) -> int:
    result = []
    idx = 0

    l1 = len(num1)
    l2 = len(num2)

    carry = 0
    for idx in range(max(l1, l2)):
        d1 = int(num1[l1 - 1 - idx]) if idx < l1 else 0
        d2 = int(num2[l2 - 1 - idx]) if idx < l2 else 0

        total = d1 + d2 + carry
        if total > 10:
            carry = 1
            total_digit = total % 10
        else:
            carry = 0
            total_digit = total
        result.insert(0, str(total_digit))

    print("".join(result))


# TODO: Move tests and add more
sum_two_str_ints("9999", "99999")
