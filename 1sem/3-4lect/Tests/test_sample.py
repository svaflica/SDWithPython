from onTest import fast_pow

def test_1():
    assert (fast_pow(2, 8) == 256), "Must be 256"

def test_2():
    assert (fast_pow(4, 15) == 4 ** 15), f"Must be {4 ** 15}"

def test_fail():
    assert False