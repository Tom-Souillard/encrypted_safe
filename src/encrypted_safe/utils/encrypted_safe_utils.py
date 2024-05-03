import random
import string

def gen_random_string(lenght: int) -> str:
    """
    Generates a random string of specified lenght using ASCII letters and digits.

    Args:
        lenght: (int) The lenght of the string to generate

    Returns:
        (str) A random string consisting of ASCII letters and digits.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=lenght))

def gen_random_tuple(lenght: int, minimum: int = 0, maximum: int = 10) -> tuple:
    """
    Generates a tuple of random integers with a specified lenght.

    Args:
        lenght: (int) number of elements in the tuple.
        minimum: (int) the minimum value of the integers.
        maximum: (int) the maximum value of the integers

    Returns:
        (tuple) tuple containing random integers.
    """
    return tuple(random.randint(minimum, maximum) for _ in range(lenght))