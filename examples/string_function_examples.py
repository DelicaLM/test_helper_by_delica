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

# Import the test helper package.
import src.test_helper_funcs as test_lib

# Import the IOPair class
from src.IOPair import IOPair

import argparse


DEFAULT_CHAR = "a"
DEFAULT_MULTI_CHAR_STR = "abc"

run_all_demos = True
run_empty_string_demo = run_all_demos or True
run_single_char_demo = run_all_demos or True
run_multi_char_string_demo = run_all_demos or True
run_multiply_string_demo = run_all_demos or True
run_concat_strings_demo = run_all_demos or True
run_remove_vowels_demo = run_all_demos or True

# Parse the runtime arguments to determine which examples we should run.
parser = argparse.ArgumentParser(description="Parser for integer examples script")
"Parser for optional runtime arguments."
parser.add_argument("--run_empty_string_demo", action="store_true",
help="Boolean flag for whether the tests that call the return zero function should be executed (optional argument).")
parser.add_argument("--run_single_char_demo", action="store_true",
help="Boolean flag for whether the tests that call the return single character function should be executed (optional "
+"argument).")
parser.add_argument("--run_multi_char_string_demo", action="store_true",
help="Boolean flag for whether the tests that call the return a string with multiple characters function should be "
+"executed (optional argument).")
parser.add_argument("--run_multiply_string_demo", action="store_true",
help="Boolean flag for whether the tests that call the multiply string function should be executed (optional "
+"argument).")
parser.add_argument("--run_concat_strings_demo", action="store_true",
help="Boolean flag for whether the tests that call the return concatenated strings function should be executed "
+ "(optional argument).")
parser.add_argument("--run_remove_vowels_demo", action="store_true",
help="Boolean flag for whether the tests that call the remove vowels from string function should be executed "
+ "(optional argument).")

# Parse the runtime arguments
args = parser.parse_args()
"Parsed runtime arguments."
run_empty_string_demo = args.run_empty_string_demo
"Runtime flag for whether we should run the empty string example."
run_single_char_demo = args.run_single_char_demo
"Runtime flag for whether we should run the single character string example."
run_multi_char_string_demo = args.run_multi_char_string_demo
"Runtime flag for whether we should run the multiple character string example."
run_multiply_string_demo = args.run_multiply_string_demo
"Runtime flag for whether we should run the multiply string example."
run_concat_strings_demo = args.run_concat_strings_demo
"Runtime flag for whether we should run the concatenate strings example."
run_remove_vowels = args.run_remove_vowels_demo
"Runtime flag for whether we should run the remove vowels demo."
# Check if the user requested to run any of the demos.
any_demos = run_empty_string_demo or run_single_char_demo or run_multi_char_string_demo or\
            run_multiply_string_demo or run_concat_strings_demo or run_remove_vowels_demo
"Boolean for whether any demos were requested by the user (through the runtime arguments)."
# By default, (if no runtime flags are provided) the script will run all of the string demos.
run_all_demos = not any_demos
"Boolean for whether all demos should be run (default behaviour if no specific demos are requested)."
# If no demos are selected, we will run all of them.
run_empty_string_demo = run_empty_string_demo or run_all_demos
run_single_char_demo = run_single_char_demo or run_all_demos
run_multi_char_string_demo = run_multi_char_string_demo or run_all_demos
run_multiply_string_demo = run_multiply_string_demo or run_all_demos
run_concat_strings_demo = run_concat_strings_demo or run_all_demos
run_remove_vowels = run_remove_vowels_demo or run_all_demos

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

if run_empty_string_demo:
    test_lib.run_func_tests(return_empty_string,
                   [IOPair((), ""),
                    IOPair(0, TypeError)],
                   test_desc="function that always returns an empty string")

if run_return_single_char_demo:
    test_lib.run_func_tests(return_single_char,
                   [IOPair((), DEFAULT_CHAR),
                    IOPair(0, TypeError)],
                   test_desc="function that returns a single character string "
                             + "(determined by the DEFAULT_CHAR constant)")

if run_return_multi_char_string_demo:
    test_lib.run_func_tests(return_multi_char_string,
                   [IOPair((), DEFAULT_MULTI_CHAR_STR),
                    IOPair(0, TypeError)],
                   test_desc="function that returns a string with more than one character "
                             + "(determined by the DEFAULT_MULTI_CHAR_STR constant)")
if run_multiply_string_demo:
    test_lib.run_func_tests(multiply_string,
                   [IOPair(("",1), ""),
                    IOPair(("a",1),"a"),
                    IOPair(("b",2),"bb"),
                    IOPair(("c", 3), "ccc"),
                    IOPair(("12", 4), "12121212"),
                    IOPair(0, TypeError)],
                   test_desc="function that returns the multiplication of a string parameter by a requested number of "
                              + "repetitions")

if run_concat_strings_demo:
    test_lib.run_func_tests(concat_strings,
                   [IOPair(("",""), ""),
                    IOPair(("a",""),"a"),
                    IOPair(("","a"), "a"),
                    IOPair(("a","b"),"ab"),
                    IOPair(("abc", "def"), "abcdef"),
                    IOPair(0, TypeError)],
                   test_desc="function that returns the concatenation of two strings")

if run_remove_vowels_demo:
    test_lib.run_func_tests(remove_vowels,
                   [IOPair("", ""),
                    IOPair("a",""),
                    IOPair("s","s"),
                    IOPair("ab","b"),
                    IOPair("abcdefgh","bcdfgh"),
                    IOPair(0, TypeError)],
                   test_desc="function that returns a copy of the string parameter with all vowels removed")


