"""
This script provides several examples of how one can use test_helper_by_delica to test boolean functions (i.e.,
functions that return True or False). We use the sample functions below to demonstrate test_bool_func from the test
helper package allows us to quickly verify that Python code accurately returns True or False for a wide range of inputs.

Functions
---------
always_true()
    Returns True.
always_false()
    Returns False.
is_int(val)
    Returns True if val is an integer and False if it is not.
can_convert_to_int(val)
    Returns True if val is an integer or can be converted to an integer, False otherwise.
"""

from test_helper_by_delica import *

run_always_true_demo = True
run_always_false_demo = True
run_is_int_demo = True
run_can_convert_to_int_demo = True
run_list_has_val_demo = True


def always_true():
    """Function that always returns True"""
    return True

def always_false():
    """Function that always returns False"""
    return False

def is_int(val):
    """Function that returns True if val is an integer and False if it is not."""
    return isinstance(val, int)

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
    test_bool_func(always_true, true_inputs=[()], test_desc="always true function")

if run_always_false_demo:
    test_bool_func( always_false, false_inputs=[()], test_desc="always false function")

if run_is_int_demo:
    test_bool_func(is_int, true_inputs=[(1,),(2,),(-10,)], false_inputs=[(1.0,),(2.0,),("",),('a',),("abc",)], test_desc="is_int function")

if run_can_convert_to_int_demo:
    test_bool_func(can_convert_to_int, true_inputs=[(1,),(2.0,),("-10",)], false_inputs=[("hello",),("1ab",),([],)],
               test_desc="can_convert_to_int function"),

if run_list_has_val_demo:
    test_bool_func(list_has_val, true_inputs=[([1],1),([1,2],2),(["a","ab","abc"],"a")],
                   false_inputs=[([],0),([1],2),([1,2,3],4),(["a",1,"b"],2)])