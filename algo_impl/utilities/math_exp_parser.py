from typing import List
import re
from adt_impl.queue import Queue


def tokenize_with_regexp(exp: str) -> List:
    return re.findall("\s*([()+*/-]|\d+)", exp)


def tokenize_davi_way(exp: str) -> List:
    queue = Queue()
    cum_digit = ""
    for c in exp.replace(" ", ""):
        if c in ["(", ")", "+", "-", "/", "*"]:
            if cum_digit != "":
                queue.enqueue(cum_digit)
                cum_digit = ""
            queue.enqueue(c)
        elif c.isdigit():
            cum_digit += c
        else:
            raise ValueError
    return [queue.dequeue() for i in range(len(queue))]


# TODO: turn the following into unit tests
exp = "((73 + ( (34- 72 ) / ( 33 -3) )) + (56 +(95 - 28) ) )"
print(f"regexp version      : {tokenize_with_regexp(exp)}")
print(f"davi version        : {tokenize_davi_way(exp)}")
