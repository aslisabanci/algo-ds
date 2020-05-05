def max_knapsack_val_multiple_selection(weights_vals: dict, cap: int) -> int:
    max_vals = [0] * (cap + 1)

    for c in range(1, cap + 1):
        sub_max = 0
        for weight, val in weights_vals.items():
            if weight <= c:
                trial_sub = max_vals[c - weight] + val
                if trial_sub > sub_max:
                    sub_max = trial_sub
        max_vals[c] = sub_max
    print(max_vals)


def max_knapsack_val_binary_selection(weights_vals: dict, cap: int) -> int:
    solutions = [[0 for c in range(cap + 1)] for w in range(len(weights_vals))]

    for idx, weight in enumerate(weights_vals):
        for c in range(1, cap + 1):
            current_best = solutions[idx - 1][c]
            if weight <= c:
                candidate = solutions[idx - 1][c - weight] + weights_vals[weight]
                current_best = max(candidate, current_best)
            solutions[idx][c] = current_best
    print(solutions)
    print(solutions[idx][c])


# TODO: Move tests and add more
pairs = {2: 1, 10: 20, 3: 3, 6: 14, 18: 100}
max_knapsack_val_multiple_selection(pairs, 15)

pairs = {5: 100, 7: 150, 3: 70}
max_knapsack_val_multiple_selection(pairs, 36)

pairs = {2: 1, 10: 20, 3: 3, 6: 14, 18: 100}
max_knapsack_val_binary_selection(pairs, 15)

pairs = {5: 100, 7: 150, 3: 70}
max_knapsack_val_binary_selection(pairs, 36)
