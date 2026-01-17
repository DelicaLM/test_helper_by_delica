"""
Script demonstrating how we can use the test helper package to validate object-oriented functions.


The following classes are defined in this file to show the diversity of class structures that the test helper package
can evaluate.

Classes
-------
EmptyClass
    Class with no attributes and no instance methods.
OneIntAttrClass
    Class with one integer attribute and no instance methods.
NoAttrOneStatMethodClass
    Class with no attributes and one static method.




"""

# Import the test helper package.
from test_helper_by_delica import *

# Import argparse for parsing runtimes flags (which determine whether each class demo is executed).
import argparse


class EmptyClass:
    """Class with no attributes and no instance methods."""
    def __init__(self):
        pass


class OneIntAttrClass:
    """Class with one integer attribute.

    Attributes
    ----------
    int_val : int
        Integer attribute value.
    """
    def __init__(self, int_val):
        """OneIntAttrClass constructor.

        Parameters
        ----------
        int_val : int
            The integer that should be stored in the new object.
        """
        self.int_val = int_val

    def __eq__(self, other):
        """Equality instance method (checks equality with another object).

        This equality function concludes that two OneIntAttrClass instances are equal if their
        integer attributes are equal.
        Parameters
        ----------
        other : OneIntAttrClass
            The other instance of this class (which contains the integer attribute that must be compared against the
            attribute value of the calling object).

        Returns
        -------
        bool
            Returns True if the two instance have the same integer attribute value.
        """
        result = False
        if isinstance(other, OneIntAttrClass):
            result = self.int_val == other.int_val
        return result

    def __str__(self):
        """Convert-to-string instance method."""
        return f"OneIntAttrClass(int_val={self.int_val})"


class NoAttrOneStatMethodClass:
    """Class with no attributes and one static method.
    """
    def __init__(self):
        """NoAttrOneStatMethodClass constructor (empty)."""
        pass

    @staticmethod
    def return_zero():
        """Static method that always returns zero."""
        return 0

class OneAttrOneMethodClass:
    """Class with one attribute and one get instance method."""
    def __init__(self, int_val):
        """OneAttrOneMethodClass constructor.

        Parameters
        ---------
        int_val : int
            The integer that should be stored in the new object.
        """
        self.int_val = int_val

    def return_int_val(self):
        """Get method for the integer attribute."""
        return self.int_val

    def __eq__(self, other):
        """Equality instance method (checks equality with another object).

        This equality function concludes that two OneAttrOneMethodClass instances are equal if their integer attributes
        are equal.

        Parameters
        ----------
        other : OneAttrOneMethodClass
            The other instance of this class (which contains the integer attribute that must be compared against the
            attribute value of the calling object).
        """
        result = False
        if isinstance(other, OneAttrOneMethodClass):
            result = self.int_val == other.int_val
        return result

    def __str__(self):
        """Convert-to-string instance method."""
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