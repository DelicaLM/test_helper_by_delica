"""Module that provides functions to generate input data for software tests."""

# Import random to randomly generate input values.
import random as rand

# Set constants for generating random values.
LARGE_INT = 100000000
SHORT_LIST_LENGTH = 10
LONG_LIST_LENGTH = 250
ATOZ_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ATOZ_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ATOZ_MIXEDCASE = ATOZ_LOWERCASE + ATOZ_UPPERCASE
DIGITS = "0123456789"
MISC_SYMBOLS = "+?/%^&*@!#$()[]{}\'\"\n"
SHORT_STRING_LENGTH = 5
LONG_STRING_LENGTH = 50

def get_rand_bool():
    """Randomly returns True or False with equal probability."""
    return rand.choice([True, False])

def get_rand_bool_list(num_bools):
    """Generates a list with random boolean elements.

    Parameters
    ----------
    num_bools : int
        Length of the list to generate.

    Returns
    -------
    list[bool]
        A list with random boolean elements.
    """
    if type(num_bools) != int:
        raise TypeError(f"Number of boolean elements must be an integer.")
    if num_bools <= 0:
        raise ValueError("Number of boolean elements must be greater than 0.")
    return [get_rand_bool() for i in range(num_bools)]

def get_rand_int():
    """Returns a random negative or positive integer."""
    return rand.randint(-LARGE_INT, LARGE_INT)

def get_rand_pos_int():
    """Returns a random positive integer."""
    return rand.randint(1, LARGE_INT)

def get_rand_neg_int():
    """Returns a random negative integer."""
    return rand.randint(-LARGE_INT, 0)

def get_rand_int_list(num_ints):
    """Generates a list with random integer elements.

    Parameters
    ----------
    num_ints : int
        Length of the list to generate.

    Returns
    -------
    list[int]
        A list with random integer elements.
    """
    assert num_ints > 0, "Number of integer elements must be greater than 0."
    if num_ints <= 0:
        raise ValueError("Number of integer elements must be greater than 0.")
    return [get_rand_int() for i in range(num_ints)]

def get_rand_pos_int_list(num_ints):
    """Generates a list with random positive integer elements (>=1).

    Parameters
    ----------
    num_ints : int
        Length of the list to generate.

    Returns
    -------
    list[int]
        A list with random positive integer elements.
        """
    assert num_ints > 0, "Number of integer elements must be greater than 0."
    if num_ints <= 0:
        raise ValueError("Number of integer elements must be greater than 0.")
    return [get_rand_pos_int() for i in range(num_ints)]

def get_rand_neg_int_list(num_ints):
    """Generates a list with random negative integer elements (<=-1).

    Parameters
    ----------
    num_ints : int
        Length of the list to generate.

    Returns
    -------
    list[int]
        A list with random negative integer elements.
        """
    assert num_ints > 0, "Number of integer elements must be greater than 0."
    if num_ints <= 0:
        raise ValueError("Number of integer elements must be greater than 0.")
    return [get_rand_pos_int() for i in range(num_ints)]


def get_rand_float():
    """Returns a random negative or positive floating point number."""
    return 2.0*rand.random()*LARGE_INT - LARGE_INT

def get_rand_pos_float():
    """Returns a random positive floating point number."""
    return rand.random()*LARGE_INT

def get_rand_neg_float():
    """Returns a random negative floating point number."""
    return -rand.random()*LARGE_INT

def get_rand_float_list(num_floats):
    """Generates a list with random positive and negative float elements.

    Parameters
    ----------
    num_floats : floats
        Length of the list to generate.

    Returns
    -------
    list[float]
        A list with random float elements.
    """
    assert num_floats > 0, "Number of float elements must be greater than 0."
    if num_floats <= 0:
        raise ValueError("Number of float elements must be greater than 0.")
    return [get_rand_float() for i in range(num_floats)]

def get_rand_letter_lowercase():
    """Returns a random lowercase a-z letter."""
    return rand.choice(ATOZ_LOWERCASE)

def get_rand_letter_uppercase():
    """Returns a random uppercase A-Z letter."""
    return rand.choice(ATOZ_UPPERCASE)

def get_rand_letter_mixedcase():
    """Returns a random lowercase (a-z) or uppercase (A-Z) letter."""
    return rand.choice(ATOZ_MIXEDCASE)

def get_rand_letter_list(list_length):
    """Generates a list with random positive and negative float elements.

    Parameters
    ----------
    list_length : int
        Length of the list to generate.

    Returns
    -------
    list[str]
        A list with random string elements that each contain a single a-z or A-Z letter.
    """
    assert list_length > 0, "List length must be greater than 0."
    if list_length <= 0:
        raise ValueError("List length must be greater than 0.")
    return [get_rand_letter_mixedcase() for i in range(list_length)]

def get_rand_az_string_lowercase(num_chars):
    """Returns a random string containing only lowercase a-z letters.

    Parameters
    ----------
    num_chars : int
        Length of the string to generate.

    Returns
    -------
    str
        A random string containing only lowercase a-z letters.
    """
    assert num_chars > 0, "String length must be greater than 0."
    if num_chars <= 0:
        raise ValueError("String length float elements must be greater than 0.")
    result = ""
    for i in range(num_chars):
        result += rand.choice(ATOZ_LOWERCASE)
    return result

def get_rand_az_string_uppercase(num_chars):
    """Returns a random string containing only uppercase A-Z letters.

    Parameters
    ----------
    num_chars : int
        Length of the string to generate.

    Returns
    -------
    str
        A random string containing only uppercase A-Z letters.
    """
    result = ""
    for i in range(num_chars):
        result += rand.choice(ATOZ_UPPERCASE)
    return result


def get_rand_az_string_mixedcase(num_chars):
    """Returns a random string upper- and lowercase letters (a-z and A-Z).

    Parameters
    ----------
    num_chars : int
        Length of the string to generate.

    Returns
    -------
    str
        A random string containing uppercase and lowercase letters.
    """
    assert num_chars > 0, "String length must be greater than 0."
    if num_chars <= 0:
        raise ValueError("String length float elements must be greater than 0.")
    result = ""
    for i in range(num_chars):
        result += rand.choice(ATOZ_MIXEDCASE)
    return result

def get_rand_az_string_list(list_length):
    """Generates a list with random string elements that only contain letters in the ranges a-z and A-Z.

    Parameters
    ----------
    list_length : int
        Length of the list to generate.

    Returns
    -------
    list[str]
        A list with random string elements that each contain multiple a-z or A-Z letters.
    """
    assert list_length > 0, "List length must be greater than 0."
    if list_length <= 0:
        raise ValueError("List length must be greater than 0.")
    min_string_length = 1
    max_string_length = LONG_STRING_LENGTH
    result = [""]*list_length
    for i in range(list_length):
        string_length = rand.randint(min_string_length, max_string_length+1)
        result[i] = get_rand_az_string_mixedcase(string_length)
    return result


