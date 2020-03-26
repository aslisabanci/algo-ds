def permutations(string, perms, prefix=""):
    if len(string) == 0:
        perms.append(prefix)
    else:
        for i in range(len(string)):
            suffix = string[0:i] + string[i+1:]
            permutations(suffix, perms, prefix+string[i])