"""
This script provides several examples of how one can use test_helper_by_delica to test object-oriented programming
functions (i.e., functions that return or use an instance of a class). We use the sample functions below to demonstrate
how run_func_tests from the test helper package allows us to quickly verify that Python code accurately uses and returns
objects for a wide range of input types.

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

class EmptyClass:
    def __init__(self):
        pass

class OneIntAttrClass:
    def __init__(self, int_val):
        self.int_val = int_val

    def __eq__(self, other):
        result = False
        if isinstance(other, OneIntAttrClass):
            result = self.int_val == other.int_val
        return result


class NoAttrOneStatMethodClass:
    def __init__(self):
        pass
    @staticmethod
    def return_zero():
        return 0

class OneAttrOneMethodClass:
    def __init__(self, int_val):
        self.int_val = int_val
    def return_int_val(self):
        return self.int_val

class TwoAttrTwoMethodClass:
    def __init__(self, int_val, str_val):
        self.int_val = int_val
        self.str_val = str_val
    def return_int_val(self):
        return self.int_val
    def return_str_val(self):
        return self.str_val

class ListAttrClass:
    def __init__(self, input_list):
        self.my_list = input_list




run_empty_class_demo = True
run_one_int_attr_class_demo = True

if run_empty_class_demo:
    run_func_tests(EmptyClass, [IOPair((),EmptyClass)],assert_type=ASSERT_TYPE,
                   test_desc="empty class constructor")

if run_one_int_attr_class_demo:
    run_func_tests(OneIntAttrClass, [IOPair(0,OneIntAttrClass(0)),
                                     IOPair(1,OneIntAttrClass(1)),
                                     IOPair(-1,OneIntAttrClass(-1))],assert_type=ASSERT_EQUAL,
                   test_desc="constructor for class with one integer attribute")