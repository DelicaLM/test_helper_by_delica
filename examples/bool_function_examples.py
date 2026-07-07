"""
This script provides several examples of how one can use src to test boolean functions (i.e.,
functions that return True or False). We use the sample functions below to demonstrate how test_bool_func from the test
helper package allows us to quickly verify that Python code accurately returns True or False for a wide range of inputs.

Functions
---------
always_true()
    Returns True.
always_false()
    Returns False.
is_int(val)
    Returns True if val is an integer and False if it is not.
is_int_error_if_false(val)
    Returns True if val is an integer and raises a TypeError if it is not.
can_convert_to_int(val)
    Returns True if val is an integer or can be converted to an integer, False otherwise.
"""

from src import test_helper_funcs as test_lib
import argparse

run_always_true_demo = False
run_always_false_demo = False
run_is_int_demo = False
run_is_int_error_if_false_demo = True
run_can_convert_to_int_demo = False
run_list_has_val_demo = False

parser = argparse.ArgumentParser(description="Parser for boolean examples script")
parser.add_argument("--run_always_true_demo", action="store_true",
help="Boolean flag for whether the tests that call the always true function should be executed (optional argument).")
parser.add_argument("--run_always_false_demo", action="store_true",
help="Boolean flag for whether the tests that call the always false should be executed (optional argument).")
parser.add_argument("--run_is_int_demo", action="store_true",
help="Boolean flag for whether the tests that call the is integer function should be executed (optional "
+ "argument).")
parser.add_argument("--run_is_int_error_if_false_demo", action="store_true",
help="Boolean flag for whether the tests that call the is integer function with a TypeError if false should be "
+ "executed (optional argument).")
parser.add_argument("--run_can_convert_to_int_demo", action="store_true",
help="Boolean flag for whether the tests that check whether an input can be converted to an integer should be "
+ "executed (optional argument).")
parser.add_argument("--run_list_has_val_demo", action="store_true",
help="Boolean flag for whether the tests that check whether a list contains an input value should be expected "
+ "(optional argument).")


def always_true():
    """Function that always returns True"""
    return True

def always_false():
    """Function that always returns False"""
    return False

def is_int(val):
    """Function that returns True if val is an integer and False if it is not."""
    return isinstance(val, int)

def is_int_error_if_false(val):
    """Function that returns True if val is an integer raises a TypeError if it is not."""
    is_int_val = isinstance(val, int)
    if not is_int_val:
        raise TypeError(f"Value {val} of type {type(val)} is not an integer.")
    return is_int_val

def can_convert_to_int(val):
    """Function that returns True if val is an integer or can be converted to an integer and False otherwise."""
    can_convert = isinstance(val, int)
    if not can_convert:
        try:
            int_val = int(val)
            can_convert = True
        except ValueError:
            can_convert = False
        except TypeError:
            can_convert = False
    return can_convert

def list_has_val(search_list, val_to_find):
    """Function that checks whether val_to_find is an element in search_list."""
    return val_to_find in search_list

if run_always_true_demo:
    test_lib.test_bool_func(always_true, true_inputs=[()], test_desc="always true function")

if run_always_false_demo:
    test_lib.test_bool_func( always_false, false_inputs=[()], test_desc="always false function")

if run_is_int_demo:
    test_lib.test_bool_func(is_int, true_inputs=[(1,),(2,),(-10,)], false_inputs=[(1.0,),(2.0,),("",),('a',),("abc",)], test_desc="is_int function")

if run_is_int_error_if_false_demo:
    test_lib.test_bool_func(is_int_error_if_false, true_inputs=[(1,),(2,),(-10,)],
                   false_inputs=[(1.0,),(2.0,),("",),('a',),("abc",)],
                   error_if_false=True, error_type=TypeError, test_desc="is_int function")


if run_can_convert_to_int_demo:
    test_lib.test_bool_func(can_convert_to_int, true_inputs=[(1,),(2.0,),("-10",)], false_inputs=[("hello",),("1ab",),([],)],
               test_desc="can_convert_to_int function"),

if run_list_has_val_demo:
    test_lib.test_bool_func(list_has_val, true_inputs=[([1],1),([1,2],2),(["a","ab","abc"],"a")],
                   false_inputs=[([],0),([1],2),([1,2,3],4),(["a",1,"b"],2)])