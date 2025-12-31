"""
This script provides several examples of how one can use test_helper_by_delica to test string functions (i.e.,
functions with a string return value). We use the sample functions below to demonstrate how run_func_tests from the
test helper package allows us to quickly verify that Python code returns accurate strings for a wide range of inputs.

Functions
---------
return_empty_string()
    Returns "".
return_single_char()
    Returns DEFAULT_CHAR (a char constant).
return_multi_char_string()
    Returns DEFAULT_CHAR (a string constant with more than one character).
return_concat_string(str1, str2)
    Returns the concatenation of str1 and str2.
return_mult_string(str_to_multiply, num_repeats)
    Returns the multiplication of a string by a requested number of repetitions
    (e.g., "ab" -> "ababab" if num_repeats == 3).
return_string_without_vowels(str_val):
    Returns the string that we obtain after removing all vowels from the input parameter.

"""



DEFAULT_CHAR = "a"
DEFAULT_MULTI_CHAR_STR = "abc"
def return_empty_string():
    """Returns empty string."""
    return ""

def return_single_char():
    """Returns single character string (output depends on the value of the DEFAULT_CHAR constant)."""
    return DEFAULT_CHAR

def return_multi_char_string():
    """Return string with multiple characters (output depends on the value of the DEFAULT_MULTI_CHAR_STR constant)."""
    return DEFAULT_MULTI_CHAR_STR

def return_concat_string(str1, str2):
    """Returns the concatenation of two strings."""
    return str1 + str2

def return_mult_string(str_to_multiply, num_repeats):
    """Returns the inputted string multiplied by a requested number of repetitions."""
    return str_to_multiply * num_repeats

def return_string_without_vowels(str_val):
    """Returns a copy of the input string with all vowels removed."""
    result = ""
    str_copy = str_val.deepcopy()
    for char in str_copy:
        if char not in "aeiou":
            result += char
    return result