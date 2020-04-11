from algo_impl import permutation


def test_permutations_empty():
    perms = []
    permutation.permutations_of("", perms)
    assert len(perms) == 1
    assert "" in perms


def test_permutations_3():
    perms = []
    permutation.permutations_of("abc", perms)
    assert "abc" in perms
    assert "cba" in perms
    assert "bac" in perms
    assert "bca" in perms
    assert "cba" in perms
    assert "cab" in perms


def test_permutations_4():
    perms = []
    permutation.permutations_of("1234", perms)
    assert "1234" in perms
    assert "2134" in perms
    assert "3124" in perms
    assert "1324" in perms
    assert "2314" in perms
    assert "3214" in perms
    assert "3241" in perms
    assert "2341" in perms
    assert "4321" in perms
    assert "3421" in perms
    assert "2431" in perms
    assert "4231" in perms
    assert "4132" in perms
    assert "1432" in perms
    assert "3412" in perms
    assert "4312" in perms
    assert "1342" in perms
    assert "3142" in perms
    assert "2143" in perms
    assert "1243" in perms
    assert "4213" in perms
    assert "2413" in perms
    assert "1423" in perms
    assert "4123" in perms
