"""
This script provides several examples of how one can use the test helper package to test boolean functions (i.e.,
functions that return True or False). We use the sample functions below to demonstrate how test_bool_func from the test
helper package allows us to quickly verify that Python code accurately returns True or False for a wide range of inputs.

Parameters
---------
---run_always_true_demo : bool, default False
    Boolean flag for whether the always true function example should be run.
---run_always_false_demo : bool, default False
    Boolean flag for whether the always false function example should be run.
---run_is_int_demo : bool, default False
    Boolean flag for whether the is int function example should be run.
---run_is_int_error_if_false_demo : bool, default False
    Boolean flag for whether the is int with type error if false function example should be run.
---run_can_convert_to_int_demo : bool, default False
    Boolean flag for whether the can conver to int function example should be run.
---run_list_has_val_demo : bool, default False
    Boolean flag for whether the list has value function example should be run.

"""

# Import the test helper package.
from src import test_helper_funcs as test_lib

# Import argparse to parse runtime arguments (which allow the user to select which demos they want to run).
import argparse

# # Variables for the runtime arguments
# run_always_true_demo = False
# run_always_false_demo = False
# run_is_int_demo = False
# run_is_int_error_if_false_demo = False
# run_can_convert_to_int_demo = False
# run_list_has_val_demo = False

# Define the optional runtime arguments
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

# Parse the runtime arguments
args = parser.parse_args()
"Parsed runtime arguments"
run_always_true_demo = args.run_always_true_demo
"Runtime flag for whether we should run the always true function example"
run_always_false_demo = args.run_always_false_demo
"Runtime flag for whether we should run the always false function example"
run_is_int_demo = args.run_is_int_demo
"Runtime flag for whether we should run the is integer function example"
run_is_int_error_if_false_demo = args.run_is_int_error_if_false_demo
"Runtime flag for whether we should run the is integer error if false function example"
run_can_convert_to_int_demo = args.run_can_convert_to_int_demo
"Runtime flag for whether we should run the can convert to int function example"
run_list_has_val_demo = args.run_list_has_val_demo
"Runtime flag for whether we should run the list has value function example"

# Check if the user requested to run any of the demos.
any_demos = run_always_true_demo or run_always_false_demo or run_is_int_demo or run_is_int_error_if_false_demo\
            or run_can_convert_to_int_demo or run_list_has_val_demo
"Boolean for whether any demos were requested by the user (through the runtime arguments)"
# By default, (if no runtime flags are provided) the script will run all of the class demos.
run_all_demos = not any_demos
"Boolean for whether all demos should be run (default behaviour if no specific demos are requested)"

# If no demos are selected, we will run all of them.
run_always_true_demo = run_always_true_demo or run_all_demos
run_always_false_demo = run_always_false_demo or run_all_demos
run_is_int_demo = run_is_int_demo or run_all_demos
run_is_int_error_if_false_demo = run_is_int_error_if_false_demo or run_all_demos
run_can_convert_to_int_demo = run_can_convert_to_int_demo or run_all_demos
run_list_has_val_demo = run_list_has_val_demo or run_all_demos


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