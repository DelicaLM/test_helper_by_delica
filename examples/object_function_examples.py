"""
Script demonstrating how we can use the test helper package to validate object-oriented functions.


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

    def __str__(self):
        return f"OneIntAttrClass(int_val={self.int_val})"



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
    def __eq__(self, other):
        result = False
        if isinstance(other, OneAttrOneMethodClass):
            result = self.int_val == other.int_val
        return result
    def __str__(self):
        return f"OneAttrOneMethodClass(int_val={self.int_val})"

class TwoAttrTwoMethodClass:
    def __init__(self, int_val, str_val):
        self.int_val = int_val
        self.str_val = str_val
    def return_int_val(self):
        return self.int_val
    def return_str_val(self):
        return self.str_val
    def __eq__(self, other):
        result = False
        if isinstance(other, TwoAttrTwoMethodClass):
            result = self.int_val == other.int_val and self.str_val == other.str_val
        return result
    def __str__(self):
        return f"TwoAttrTwoMethodClass(int_val={self.int_val}, str_val={self.str_val})"

class ListAttrClass:
    def __init__(self, input_list):
        self.my_list = input_list
    def calc_list_sum(self):
        list_sum = 0
        for list_item in self.my_list:
            if type(list_item) == int or type(list_item) == float:
                list_sum += list_item
        return list_sum




run_empty_class_demo = True
run_one_int_attr_class_demo = True
run_no_attr_one_stat_method_demo = True
run_one_attr_one_method_demo = True
run_two_attr_two_method_demo = True
run_list_attr_class_demo = True

if run_empty_class_demo:
    run_func_tests(EmptyClass, [IOPair((),EmptyClass)],assert_type=ASSERT_TYPE,
                   test_desc="empty class constructor")

if run_one_int_attr_class_demo:
    run_func_tests(OneIntAttrClass, [IOPair(0,OneIntAttrClass(0)),
                                     IOPair(1,OneIntAttrClass(1)),
                                     IOPair(-1,OneIntAttrClass(-1))],
                   test_desc="constructor for class with one integer attribute")

if run_no_attr_one_stat_method_demo:
    run_func_tests(NoAttrOneStatMethodClass.return_zero,[IOPair((),0)],
                   test_desc="static int method for class with no attribute")

if run_one_attr_one_method_demo:
    run_func_tests(OneAttrOneMethodClass, [IOPair(1, OneAttrOneMethodClass(1)),
                                           IOPair(100, OneAttrOneMethodClass(100)),
                                           IOPair((), TypeError)],
                   test_desc="constructor for class with one int attribute and one get method")
    run_func_tests(OneAttrOneMethodClass(30).return_int_val, [IOPair((), 30),
                                           IOPair((2), TypeError)],
                   test_desc="get method for class with one int attribute")

if run_two_attr_two_method_demo:
    run_func_tests(TwoAttrTwoMethodClass, [IOPair((1,"hello"), TwoAttrTwoMethodClass(1,"hello")),
                                           IOPair((100,"100"), TwoAttrTwoMethodClass(100,"100")),
                                           IOPair((), TypeError), IOPair(1, TypeError)],
                   test_desc="constructor for class with two attributes (one int and one string) and two get methods")
    run_func_tests(TwoAttrTwoMethodClass(500, "hi").return_int_val,
                   [IOPair((), 500)],
                   test_desc="get int method for class with two int attributes and two get methods")
    run_func_tests(TwoAttrTwoMethodClass(500, "hi").return_str_val,
                   [IOPair((), "hi")],
                   test_desc="get string method for class with two int attributes and two get methods")