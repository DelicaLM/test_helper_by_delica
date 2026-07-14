"""
This script provides several examples of how one can use the test helper package to validate functions that return
integer values. The optional runtime arguments below allow the user to select which integer examples they would like to
run. If no runtime flags are used, this script will run all of the built-in integer examples.

Parameters
----------
---run_return_zero_demo : bool, default False
    Boolean flag for whether the return zero function example should be run.
---run_return_int_plus_one_demo : bool, default False
    Boolean flag for whether the return int plus one function example should be run.
---run_return_neg_int_demo : bool, default False
    Boolean flag for whether the return negative integer function example should be run.
---run_return_string_length_demo : bool, default False
    Boolean flag for whether the return string length function example should be run.
---run_add_ints_demo : bool, default False
    Boolean flag for whether the add integers function example should be run.
---run_calc_int_list_sum_demo : bool, default False
    Boolean flag for whether the calculate list sum function example should be run.
"""

# Import the test helper package.
from src import test_helper_funcs as test_lib

# Import the IOPair class.
from src.IOPair import IOPair

# Import argparse for the optional runtime arguments (which allow the user to choose which demos they want to run).
import argparse

# Configure the runtime argument parser.
parser = argparse.ArgumentParser(description="Parser for integer examples script")
"Runtime argument parser"
parser.add_argument("--run_return_zero_demo", action="store_true",
help="Boolean flag for whether the tests that call the return zero function should be executed (optional argument).")
parser.add_argument("--run_return_int_plus_one_demo", action="store_true",
help="Boolean flag for whether the tests that call the return input plus one function should be executed (optional "
+"argument).")
parser.add_argument("--run_return_neg_int_demo", action="store_true",
help="Boolean flag for whether the tests that call the return negative of an input integer function should be executed "
+"(optional argument).")
parser.add_argument("--run_return_string_length_demo", action="store_true",
help="Boolean flag for whether the tests that call the return string length function should be executed (optional "
+"argument).")
parser.add_argument("--run_add_ints_demo", action="store_true",
help="Boolean flag for whether the tests that call the add two integers function should be executed (optional "
+"argument).")
parser.add_argument("--run_calc_int_list_sum_demo", action="store_true",
help="Boolean flag for whether the tests that call the calculate sum of an integer list function should be executed "
+"(optional argument).")

# Parse the runtime arguments
args = parser.parse_args()
"Parsed runtime arguments"
run_return_zero_demo = args.run_return_zero_demo
"Runtime flag for whether we should run the return zero function example"
run_return_int_plus_one_demo = args.run_return_int_plus_one_demo
"Runtime flag for whether we should run the return int plus one function example"
run_return_neg_int_demo = args.run_return_neg_int_demo
"Runtime flag for whether we should run the return negative integer function example"
run_return_string_length_demo = args.run_return_string_length_demo
"Runtime flag for whether we should run the return string length function example"
run_add_ints_demo = args.run_add_ints_demo
"Runtime flag for whether we should run the add integers function example"
run_calc_int_list_sum_demo = args.run_calc_int_list_sum_demo
"Runtime flag for whether we should run the calculate integer list sum function example"

# Check if the user requested to run any of the demos.
any_demos = run_return_zero_demo or run_return_int_plus_one_demo or run_return_neg_int_demo or\
            run_return_string_length_demo or run_add_ints_demo or run_calc_int_list_sum_demo
"Boolean for whether any demos were requested by the user (through the runtime arguments)"
# By default, (if no runtime flags are provided) the script will run all of the int demos.
run_all_demos = not any_demos
"Boolean for whether all demos should be run (default behaviour if no specific demos are requested)"
# If no demos are selected, we will run all of them.
run_return_zero_demo = run_return_zero_demo or run_all_demos
run_return_int_plus_one_demo = run_return_int_plus_one_demo or run_all_demos
run_return_neg_int_demo = run_return_neg_int_demo or run_all_demos
run_return_string_length_demo = run_return_string_length_demo or run_all_demos
run_add_ints_demo = run_add_ints_demo or run_all_demos
run_calc_int_list_sum_demo = run_calc_int_list_sum_demo or run_all_demos

def return_zero():
    """Returns zero."""
    return 0

def return_int_plus_one(int_val):
    """Returns the input parameter int_val plus one."""
    return int_val + 1

def return_neg_int(int_val):
    """Returns the negative of the input parameter int_val."""
    return -int_val

def return_string_length(input_str):
    """Returns the length of the string parameter input_str."""
    return len(input_str)

def add_ints(int1, int2):
    """Returns the sum of two integers (int1 and int2)."""
    return int1 + int2

def calc_int_list_sum(input_list):
    """Returns the sum of all integers in a list of integers (input_list)."""
    list_sum = 0
    if type(input_list) == list:
        for item in input_list:
            if type(item) == int:
                list_sum += item
    return list_sum

if run_return_zero_demo:
    test_lib.run_func_tests(return_zero,
                   [IOPair((),0),
                                 IOPair(0,TypeError)],
                   test_desc="function that always returns zero (as an int)")

if run_return_int_plus_one_demo:
    test_lib.run_func_tests(return_int_plus_one,
                   [IOPair(0,1),
                    IOPair(5,6),
                    IOPair(100,101),
                    IOPair(-5, -4)],
                   test_desc="function that returns the sum of one and an integer parameter")

if run_return_neg_int_demo:
    test_lib.run_func_tests(return_neg_int,
                   [IOPair(0,0),
                    IOPair(-1,1),
                    IOPair(6,-6),
                    IOPair(-1000, 1000),
                    IOPair((0,0), TypeError)],
                   test_desc="function that returns the negative of an integer parameter")

if run_return_string_length_demo:
    test_lib.run_func_tests(return_string_length,
                   [IOPair("",0),
                    IOPair("a",1),
                    IOPair("abc",3),
                    IOPair("abcdef",6),
                    IOPair(5, TypeError)],
                   test_desc="function that returns the number of characters in a string parameter")

if run_add_ints_demo:
    test_lib.run_func_tests(add_ints,[IOPair((2, 2), 4),
                             IOPair((1, 7), 8),
                             IOPair((-10, 5), -5),
                             IOPair((-100000, -150000),-250000),
                             IOPair(1, TypeError),
                             IOPair(([],1), TypeError),
                             IOPair(("",2), TypeError)],
                   test_desc="function that returns the sum of two integers")

if run_calc_int_list_sum_demo:
    test_lib.run_func_tests(calc_int_list_sum,[IOPair([], 0),
                                               IOPair([1], 1),
                                               IOPair([1, 2], 3),
                                               IOPair([1, 2, 3], 6)],
                            test_desc="function that returns the sum of all elements in an integer list")










