from adt_impl.stack import Stack


def reverse_str(input: str) -> str:
    """Reverses a string using a Stack data structure.
    
    Arguments:
        input {str} -- string to reverse
    
    Returns:
        str -- reversed string
    """
    stack = Stack()
    for c in input:
        stack.push(c)
    return "".join([stack.pop() for c in range(len(stack))])


# TODO: add unit tests
print(reverse_str("whaeva"))
