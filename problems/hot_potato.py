from collections import deque
from typing import List


def hot_potato_winner(players: List[str], turns: int) -> str:
    circle = deque()
    for p in players:
        circle.appendleft(p)

    while len(circle) > 1:
        for _ in range(turns):
            circle.appendleft(circle.pop())
        print(f"hot potato left at: {circle.pop()}")

    return circle.pop()


print(hot_potato_winner(("asli", "doctor", "donna noble", "rose", "river", "amy"), 9))
