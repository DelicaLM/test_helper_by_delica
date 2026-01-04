"""
This script provides several examples of how one can use test_helper_by_delica to test integer functions (i.e.,
functions that return an integer value). We use the sample functions below to demonstrate how run_func_tests from the
test helper package allows us to quickly verify that Python code returns accurate integer values for a wide range of
inputs.

Functions
---------
return_zero()
    Returns 0.
return_int_plus_one(int_val)
    Returns the sum of one and the integer parameter.
return_neg_int(int_val)
    Returns the negative of the integer parameter.
return_string_length(input_str)
    Returns the number of characters in the string parameter.
add_ints(int1, int2)
    Returns the sum of two integers.
calc_int_list_sum(int_list)
    Returns the sum of all the values in a list of integers.

"""

from test_helper_by_delica import *

run_all_demos = True
run_return_zero_demo = run_all_demos or True
run_return_int_plus_one_demo = run_all_demos or True
run_return_neg_int_demo = run_all_demos or True
run_return_string_length_demo = run_all_demos or True
run_add_ints_demo = run_all_demos or True
run_calc_int_list_sum_demo = run_all_demos or True


def return_zero():
    return 0

def return_int_plus_one(int_val):
    return int_val + 1

def return_neg_int(int_val):
    return -int_val

def return_string_length(input_str):
    return len(input_str)

def add_ints(int1, int2):
    return int1 + int2

def calc_int_list_sum(input_list):
    list_sum = 0
    if type(input_list) == list:
        for item in input_list:
            if type(item) == int:
                list_sum += item
    return list_sum

if run_return_zero_demo:
    run_func_tests(return_zero,
                   [IOPair((),0),
                                 IOPair(0,TypeError)],
                   test_desc="function that always returns zero (as an int)")

if run_return_int_plus_one_demo:
    run_func_tests(return_int_plus_one,
                   [IOPair(0,1),
                    IOPair(5,6),
                    IOPair(100,101),
                    IOPair(-5, -4)],
                   test_desc="function that returns the sum of one and an integer parameter")

if run_return_neg_int_demo:
    run_func_tests(return_neg_int,
                   [IOPair(0,0),
                    IOPair(-1,1),
                    IOPair(6,-6),
                    IOPair(-1000, 1000),
                    IOPair((0,0), TypeError)],
                   test_desc="function that returns the negative of an integer parameter")

if run_return_string_length_demo:
    run_func_tests(return_string_length,
                   [IOPair("",0),
                    IOPair("a",1),
                    IOPair("abc",3),
                    IOPair("abcdef",6),
                    IOPair(5, TypeError)],
                   test_desc="function that returns the number of characters in a string parameter")

if run_add_ints_demo:
    run_func_tests(add_ints,[IOPair((2, 2), 4),
                             IOPair((1, 7), 8),
                             IOPair((-10, 5), -5),
                             IOPair((-100000, -150000),-250000),
                             IOPair(1, TypeError),
                             IOPair(([],1), TypeError),
                             IOPair(("",2), TypeError)],
                   test_desc="function that returns the sum of two integers")










