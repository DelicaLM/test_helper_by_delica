"""
This script provides several examples of how one can use src to test string functions (i.e.,
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
multiply_string(str_to_multiply, num_repeats)
    Returns the multiplication of a string by a requested number of repetitions
    (e.g., "ab" -> "ababab" if num_repeats == 3).
concat_strings(str1, str2)
    Returns the concatenation of str1 and str2.
remove_vowels(str_val):
    Returns the string that we obtain after removing all vowels from the input parameter.

"""
from src import *
import argparse


DEFAULT_CHAR = "a"
DEFAULT_MULTI_CHAR_STR = "abc"

run_all_demos = True
run_return_empty_string_demo = run_all_demos or True
run_return_single_char_demo = run_all_demos or True
run_return_multi_char_string_demo = run_all_demos or True
run_multiply_string_demo = run_all_demos or True
run_concat_strings_demo = run_all_demos or True
run_remove_vowels_demo = run_all_demos or True

parser = argparse.ArgumentParser(description="Parser for integer examples script")
parser.add_argument("--run_return_empty_string_demo", action="store_true",
help="Boolean flag for whether the tests that call the return zero function should be executed (optional argument).")
parser.add_argument("--run_return_single_char_demo", action="store_true",
help="Boolean flag for whether the tests that call the return single character function should be executed (optional "
+"argument).")
parser.add_argument("--run_return_multi_char_string_demo", action="store_true",
help="Boolean flag for whether the tests that call the return a string with multiple characters function should be "
+"executed (optional argument).")
parser.add_argument("--run_multiply_string_demo", action="store_true",
help="Boolean flag for whether the tests that call the multiply string function should be executed (optional "
+"argument).")
parser.add_argument("--run_concat_strings_demo", action="store_true",
help="Boolean flag for whether the tests that call the return concatenate strings function should be executed "
+ "(optional argument).")

def return_empty_string():
    """Returns empty string."""
    return ""

def return_single_char():
    """Returns single character string (output depends on the value of the DEFAULT_CHAR constant)."""
    return DEFAULT_CHAR

def return_multi_char_string():
    """Return string with multiple characters (output depends on the value of the DEFAULT_MULTI_CHAR_STR constant)."""
    return DEFAULT_MULTI_CHAR_STR

def concat_strings(str1, str2):
    """Returns the concatenation of two strings."""
    return str1 + str2

def multiply_string(str_to_multiply, num_repeats):
    """Returns the inputted string multiplied by a requested number of repetitions."""
    return str_to_multiply * num_repeats

def remove_vowels(str_val):
    """Returns a copy of the input string with all vowels removed."""
    result = ""
    str_copy = str_val + ""
    for char in str_copy:
        if char not in "aeiou":
            result += char
    return result

if run_return_empty_string_demo:
    run_func_tests(return_empty_string,
                   [IOPair((), ""),
                    IOPair(0, TypeError)],
                   test_desc="function that always returns an empty string")

if run_return_single_char_demo:
    run_func_tests(return_single_char,
                   [IOPair((), DEFAULT_CHAR),
                    IOPair(0, TypeError)],
                   test_desc="function that returns a single character string "
                             + "(determined by the DEFAULT_CHAR constant)")

if run_return_multi_char_string_demo:
    run_func_tests(return_multi_char_string,
                   [IOPair((), DEFAULT_MULTI_CHAR_STR),
                    IOPair(0, TypeError)],
                   test_desc="function that returns a string with more than one character "
                             + "(determined by the DEFAULT_MULTI_CHAR_STR constant)")
if run_multiply_string_demo:
    run_func_tests(multiply_string,
                   [IOPair(("",1), ""),
                    IOPair(("a",1),"a"),
                    IOPair(("b",2),"bb"),
                    IOPair(("c", 3), "ccc"),
                    IOPair(("12", 4), "12121212"),
                    IOPair(0, TypeError)],
                   test_desc="function that returns the multiplication of a string parameter by a requested number of "
                              + "repetitions")

if run_concat_strings_demo:
    run_func_tests(concat_strings,
                   [IOPair(("",""), ""),
                    IOPair(("a",""),"a"),
                    IOPair(("","a"), "a"),
                    IOPair(("a","b"),"ab"),
                    IOPair(("abc", "def"), "abcdef"),
                    IOPair(0, TypeError)],
                   test_desc="function that returns the concatenation of two strings")

if run_remove_vowels_demo:
    run_func_tests(remove_vowels,
                   [IOPair("", ""),
                    IOPair("a",""),
                    IOPair("s","s"),
                    IOPair("ab","b"),
                    IOPair("abcdefgh","bcdfgh"),
                    IOPair(0, TypeError)],
                   test_desc="function that returns a copy of the string parameter with all vowels removed")


