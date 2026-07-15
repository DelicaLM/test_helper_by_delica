"""
This script provides several examples of how one can use the test helper package to validate functions that receive
or generate string values. The optional runtime arguments below allow the user to select which string examples they
would like to run. If no runtime flags are used, this script will run all of the built-in string examples.

Parameters
----------
---run_empty_string_demo : bool, default False
    Boolean flag for whether the empty string example should be run.
---run_single_char_demo : bool, default False
    Boolean flag for whether the single character string example should be run.
---run_multi_char_demo : bool, default False
    Boolean flag for whether the multiple-character string example should be run.
---run_multiply_string_demo : bool, default False
    Boolean flag for whether the multiply string example should be run.
---run_concat_strings_demo : bool, default False
    Boolean flag for whether the concatenate strings example should be run.
---run_remove_vowels_demo : bool, default False
    Boolean flag for whether the remove vowels example should be run.
"""

# Import the test helper package.
import src.test_helper_funcs as test_lib

# Import the IOPair class.
from src.IOPair import IOPair

# Import argparse to parse the optional runtime arguments.
import argparse

# Declare default strings to use in our tests.
DEFAULT_CHAR = "a"
"Default one-character string."
DEFAULT_MULTI_CHAR_STR = "abc"
"Default multiple-character string."

# Parse the runtime arguments to determine which examples we should run.
parser = argparse.ArgumentParser(description="Parser for string examples script")
"Parser for optional runtime arguments."
parser.add_argument("--run_empty_string_demo", action="store_true",
help="Boolean flag for whether the tests that call the return empty string function should be executed "
     + "(optional argument).")
parser.add_argument("--run_single_char_demo", action="store_true",
help="Boolean flag for whether the tests that call the return single character function should be executed (optional "
+"argument).")
parser.add_argument("--run_multi_char_demo", action="store_true",
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
run_multi_char_demo = args.run_multi_char_demo
"Runtime flag for whether we should run the multiple character string example."
run_multiply_string_demo = args.run_multiply_string_demo
"Runtime flag for whether we should run the multiply string example."
run_concat_strings_demo = args.run_concat_strings_demo
"Runtime flag for whether we should run the concatenate strings example."
run_remove_vowels_demo = args.run_remove_vowels_demo
"Runtime flag for whether we should run the remove vowels demo."
# Check if the user requested to run any of the demos.
any_demos = run_empty_string_demo or run_single_char_demo or run_multi_char_demo or\
            run_multiply_string_demo or run_concat_strings_demo or run_remove_vowels_demo
"Boolean for whether any demos were requested by the user (through the runtime arguments)."
# By default, (if no runtime flags are provided) the script will run all of the string demos.
run_all_demos = not any_demos
"Boolean for whether all demos should be run (default behaviour if no specific demos are requested)."
# If no demos are selected, we will run all of them.
run_empty_string_demo = run_empty_string_demo or run_all_demos
run_single_char_demo = run_single_char_demo or run_all_demos
run_multi_char_demo = run_multi_char_demo or run_all_demos
run_multiply_string_demo = run_multiply_string_demo or run_all_demos
run_concat_strings_demo = run_concat_strings_demo or run_all_demos
run_remove_vowels_demo = run_remove_vowels_demo or run_all_demos

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

if run_single_char_demo:
    test_lib.run_func_tests(return_single_char,
                   [IOPair((), DEFAULT_CHAR),
                    IOPair(0, TypeError)],
                   test_desc="function that returns a single character string "
                             + "(determined by the DEFAULT_CHAR constant)")

if run_multi_char_demo:
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


