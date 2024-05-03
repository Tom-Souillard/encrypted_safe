from src.encrypted_safe.utils.encrypted_safe_utils import gen_random_tuple, gen_random_string

def test_gen_random_string():
    length = 10
    result = gen_random_string(length)

    assert len(result) == length
    assert isinstance(result, str)
    assert all(carac in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" for carac in result)

def test_gen_random_tuple():
    length = 9
    minimum = 0
    maximum = 10
    result = gen_random_tuple(length, minimum, maximum)

    assert len(result) == length
    assert isinstance(result, tuple)
    assert all(minimum <= elt <= maximum for elt in result)