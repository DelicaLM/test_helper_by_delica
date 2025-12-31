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
    Returns int_val + 1.
return_calc_int_list_sum(int_val)
    Returns int_val + 1.
is_int(val)
    Returns True if val is an integer and False if it is not.
is_int_error_if_false(val)
    Returns True if val is an integer and raises a TypeError if it is not.
can_convert_to_int(val)
    Returns True if val is an integer or can be converted to an integer, False otherwise.
"""

from test_helper_by_delica import *

run_return_zero_demo = True
run_int_plus_one_demo = True
run_calc_int_list_sum_demo = False
run_is_int_demo = False
run_is_int_error_if_false_demo = True
run_can_convert_to_int_demo = False
run_list_has_val_demo = False

def return_zero():
    return 0

def return_int_plus_one(int_val):
    return int_val + 1

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

if run_int_plus_one_demo:
    run_func_tests(return_int_plus_one,
                   [IOPair(0,1)],)










