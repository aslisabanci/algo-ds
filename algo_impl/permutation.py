def permutations_of(string, perms, prefix=""):
    if len(string) == 0:
        perms.append(prefix)
    else:
        for i in range(len(string)):
            suffix = string[0:i] + string[i + 1 :]
            permutations_of(suffix, perms, prefix + string[i])
