"""
Script demonstrating how we can use the test helper package to validate object-oriented functions.

Parameters
----------
--run_empty_class_demo : bool, default False

"""

# Import the test helper package.
import src.test_helper_funcs as test_helper

# Import the IOPair class
from src.IOPair import IOPair

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
        ----------
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
    """Class with two attributes and two get instance methods.

    Attributes
    ----------
    int_val : int
        An integer attribute.
    str_val : str
        A string attribute.
    """
    def __init__(self, int_val, str_val):
        """TwoAttrTwoMethodClass constructor.

        Parameters
        ----------
        int_val : int
            The integer that should be stored in the new object.
        str_val : str
            The string that should be stored in the new object."""
        self.int_val = int_val
        self.str_val = str_val

    def return_int_val(self):
        """Get method for the integer attribute."""
        return self.int_val

    def return_str_val(self):
        """Get method for the string attribute."""
        return self.str_val

    def __eq__(self, other):
        """Equality instance method (checks equality with another object).

        This equality function concludes that two TwoAttrTwoMethodClass instances are equal if their integer attributes
        and their string attributes are both identical.

        Parameters
        ----------
        other : TwoAttrTwoMethodClass
            The other instance of this class (which contains the integer and string attributes that must be compared
            against the attributes values of the calling object).

        Returns
        -------
        bool
            Returns True if the two instance have the same integer and string attribute values.
        """
        result = False
        if isinstance(other, TwoAttrTwoMethodClass):
            result = self.int_val == other.int_val and self.str_val == other.str_val
        return result

    def __str__(self):
        """Convert-to-string instance method."""
        return f"TwoAttrTwoMethodClass(int_val={self.int_val}, str_val={self.str_val})"

class ListAttrClass:
    """Class with one integer list attribute and a get list sum function.

    Attributes
    ----------
    my_list : list[int]
        A list of integers.
    """
    def __init__(self, input_list):
        """ListAttrClass constructor.

        Parameters
        ----------
        input_list : list[int]
            The list of integers that should be stored in the new object.
        """
        self.my_list = input_list

    def calc_list_sum(self):
        """Instance method for calculating the sum of all the values in the integer list."""
        list_sum = 0
        for list_item in self.my_list:
            if type(list_item) == int or type(list_item) == float:
                list_sum += list_item
        return list_sum


# Define runtime flags for determining which classes should be tested.
parser = argparse.ArgumentParser(description="Parser for object examples script")
"Parser for runtime arguments"
# Definition of the flag for running the empty class demo.
parser.add_argument("--run_empty_class_demo", action="store_true",
    help="Boolean flag for whether the tests that use the empty class (no attributes & no methods) should be executed "
         + "(optional argument).")
# Definition of the flag for running the class with one integer attribute demo.
parser.add_argument("--run_one_int_attr_demo", action="store_true",
    help="Boolean flag for whether the tests that use the one integer attribute class should be executed (optional "
         + "argument).")
# Definition of the flag for running the no attribute one static method class demo.
parser.add_argument("--run_no_attr_one_stat_method_demo", action="store_true",
    help="Boolean flag for whether the tests that use the class with no attributes and one static method should be "
         + "executed (optional argument).")
# Definition of the flag for running the one attribute one get method class demo.
parser.add_argument("--run_one_attr_one_method_demo", action="store_true",
    help="Boolean flag for whether the tests that use the class with one attribute and one get method should be "
         + "executed (optional argument).")
# Definition of the flag for running two attribute two get method class demo.
parser.add_argument("--run_two_attr_two_method_demo", action="store_true",
    help="Boolean flag for whether the tests that use the class with two attributes and two get methods should be "
         + "executed (optional argument).")
# Definition of the flag for running the list attribute class demo
parser.add_argument("--run_list_attr_demo", action="store_true",
    help="Boolean flag for whether the tests that use the class with one list attribute should be executed (optional "
         + "argument).")
args = parser.parse_args()
"Parsed runtime arguments"
run_empty_class_demo = args.run_empty_class_demo
"Runtime flag for whether we should run the empty class (no attributes & no methods) example"
run_one_int_attr_demo = args.run_one_int_attr_demo
"Runtime flag for whether we should run the one integer attribute class example"
run_no_attr_one_stat_method_demo = args.run_no_attr_one_stat_method_demo
"Runtime flag for whether we should run the no attributes and one static method class example"
run_one_attr_one_method_demo = args.run_one_attr_one_method_demo
"Runtime flag for whether we should run the one attribute and one method class example"
run_two_attr_two_method_demo = args.run_two_attr_two_method_demo
"Runtime flag for whether we should run the two attributes and two methods class example"
run_list_attr_demo = args.run_list_attr_demo
"Runtime flag for whether we should run the list attribute class example"
# Check if the user requested to run any of the demos.
any_demos = run_empty_class_demo or run_one_int_attr_demo or run_no_attr_one_stat_method_demo \
            or run_one_attr_one_method_demo or run_two_attr_two_method_demo or run_list_attr_demo
"Boolean for whether any demos were requested by the user (through the runtime arguments)"
# By default (if no runtime flags are provided), the script will run all of the class demos.
run_all_demos = not any_demos
"Boolean for whether all demos should be run (default behaviour if no specific demos are requested)"

if run_empty_class_demo:
    test_helper.run_func_tests(EmptyClass, [IOPair((),EmptyClass)],assert_type=test_helper.ASSERT_TYPE,
                   test_desc="empty class constructor")

if run_one_int_attr_demo:
    test_helper.run_func_tests(OneIntAttrClass, [IOPair(0,OneIntAttrClass(0)),
                                     IOPair(1,OneIntAttrClass(1)),
                                     IOPair(-1,OneIntAttrClass(-1))],
                   test_desc="constructor for class with one integer attribute")

if run_no_attr_one_stat_method_demo:
    test_helper.run_func_tests(NoAttrOneStatMethodClass.return_zero,[IOPair((),0)],
                   test_desc="static int method for class with no attribute")

if run_one_attr_one_method_demo:
    test_helper.run_func_tests(OneAttrOneMethodClass, [IOPair(1, OneAttrOneMethodClass(1)),
                                           IOPair(100, OneAttrOneMethodClass(100)),
                                           IOPair((), TypeError)],
                   test_desc="constructor for class with one int attribute and one get method")
    test_helper.run_func_tests(OneAttrOneMethodClass(30).return_int_val, [IOPair((), 30),
                                           IOPair((2), TypeError)],
                   test_desc="get method for class with one int attribute")

if run_two_attr_two_method_demo:
    test_helper.run_func_tests(TwoAttrTwoMethodClass, [IOPair((1,"hello"), TwoAttrTwoMethodClass(1,"hello")),
                                           IOPair((100,"100"), TwoAttrTwoMethodClass(100,"100")),
                                           IOPair((), TypeError), IOPair(1, TypeError)],
                   test_desc="constructor for class with two attributes (one int and one string) and two get methods")
    test_helper.run_func_tests(TwoAttrTwoMethodClass(500, "hi").return_int_val,
                   [IOPair((), 500)],
                   test_desc="get int method for class with two int attributes and two get methods")
    test_helper.run_func_tests(TwoAttrTwoMethodClass(500, "hi").return_str_val,
                   [IOPair((), "hi")],
                   test_desc="get string method for class with two int attributes and two get methods")