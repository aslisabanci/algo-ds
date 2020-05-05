from adt_impl.stack import Stack


def balanced_parantheses(input: str) -> bool:
    """Checks if a given string has balanced opening and closing parantheses, i.e "(" and ")"
    
    Arguments:
        input {str} -- Input string to check
    
    Returns:
        bool -- True if balanced, False otherwise
    """
    stack = Stack()
    if len(input) == 0:
        return True
    for c in input:
        if c == "(":
            stack.push(c)
        elif c == ")":
            # the stack shouldn't be empty when we see a closing parantheses
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()


# # TODO: add unit tests
print(balanced_parantheses("   ((()))"))
print(balanced_parantheses("((())"))
print(balanced_parantheses("if len(string) == 0: return True"))
print(balanced_parantheses("return True if stack.size()==0 else False)"))
