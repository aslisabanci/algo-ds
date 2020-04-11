from algo_impl import prime


def test_is_prime():
    assert prime.is_prime(5) == True


def test_is_not_prime():
    assert prime.is_prime(33) == False


def test_is_not_prime_perfect_square():
    assert prime.is_prime(25) == False


def test_is_not_prime_by_definition():
    assert prime.is_prime(-5) == False
    assert prime.is_prime(0) == False
    assert prime.is_prime(1) == False
