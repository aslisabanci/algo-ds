from collections import deque


def is_palindrome(string: str) -> bool:
    """Checks if the given string is a palindrome or not; i.e if the string is spelled the same both forward and backward. Ex: aibohphobia, kayak, Live not on evil, Reviled did I live, said I, as evil I did deliver

    Arguments:
        string {str} -- String to check

    Returns:
        bool -- True if the string is a palindrome, False otherwise.
    """
    chars_dequeu = deque(str.lower(string.replace(" ", "")))
    while len(chars_dequeu) > 1:
        first = chars_dequeu.popleft()
        last = chars_dequeu.pop()
        if first != last:
            return False
    return True


# TODO: proper unit tests
print(is_palindrome("kayak"))
print(is_palindrome("Live not on evil"))
