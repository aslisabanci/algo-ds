def longest_common_subseq(str1: str, str2: str) -> str:
    l1 = len(str1)
    l2 = len(str2)

    solutions = [[0 for c2 in range(l2 + 1)] for c1 in range(l1 + 1)]

    for c1 in range(1, l1 + 1):
        for c2 in range(1, l2 + 1):
            if str1[c1 - 1] == str2[c2 - 1]:
                solutions[c1][c2] = solutions[c1 - 1][c2 - 1] + 1

            else:
                cand1 = solutions[c1 - 1][c2]
                cand2 = solutions[c1][c2 - 1]
                solutions[c1][c2] = max(cand1, cand2)

    return solutions[l1][l2]


# TODO: Move tests and add more
print(longest_common_subseq("cookie dough", "oki doki"))
