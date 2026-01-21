"""Script to test the functions in the test helper package.

The following functions are defined to help us evaluate the package on a wide range of code.
Functions
---------
no_param_no_return()
    Function with no parameters and no return value.
one_param_no_return(int_val)
    Function with one integer parameter and no return value.
two_param_no_return(int_val1, int_val2)
    Function with two integer parameters and no return value.
no_param_one_return()
    Returns the default integer constant defined below.
no_param_two_return()
    Function with two integer return values (the default integer constant and the default integer constant plus one).
always_true()
    Returns True.
always_false()
    Returns False.

Constants
---------
DEFAULT_INT : int
    The default integer value that should be returned by a function (makes it easier to standardize tests).

"""
import test_helper_by_delica.test_helper_funcs as test_lib
from test_helper_by_delica.IOPair import IOPair

DEFAULT_INT = 0
DEFAULT_RETURN_VAL = DEFAULT_INT

test_run_single_test = True
test_run_func_tests = False
test_test_bool_func = False

test_with_no_param_no_return = False
test_with_one_param_no_return = False
test_with_two_param_no_return = False
test_with_no_param_one_return = False
test_with_no_param_two_return = False
test_with_always_true = True
test_with_always_false = False


def no_param_no_return():
    """Function with no parameters and no return value."""
    return

def one_param_no_return(int_val):
    """Function with one integer parameter and no return value.

    Parameters
    ----------
    int_val : int
        An integer value.
    """
    unused_int_val = int_val + 1
    return

def two_param_no_return(int_val1, int_val2):
    """Function with two integer parameters and no return value.

    Parameters
    ----------
    int_val1 : int
        The first integer parameter.
    int_val2 : int
        The second integer parameter.
    """
    unused_int_val1 = int_val1 + 1
    unused_int_val2 = int_val2 + 1
    return

def no_param_one_return():
    """Function with no parameters and one integer return value.

    Returns
    -------
    int
        This function returns the default integer value constant that is defined at the top of this file.
    """
    return DEFAULT_INT


def no_param_two_return():
    """Function with no parameters and two integer return values.

    Returns
    -------
    default_int : int
        The default integer constant from the top of this file.
    default_int_plus_one : int
        The next integer value after the default integer constant.
    """
    return DEFAULT_INT, DEFAULT_INT + 1

# Test the run-single-test function in the test helper package.
if test_run_single_test:
    print("TESTING RUN_SINGLE_TEST FUNCTION")
    if test_with_no_param_no_return:
        #Test whether the run-single-test function correctly handles a test function with no parameters and no output.
        #Success Case: The run-single-test function should conclude that the no-param-no-return function
        #              is working properly when it returns nothing.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_no_return,(),(),test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(True,),
                                 test_desc="run-single-test function on test function with no parameters and no return "
                                           + "value (success case)")
        #Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output from
        #           no-param-no-return does not match the actual output.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_no_return,(),(True,),test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with no parameters and no return "
                                           + "value (fail case)")
    if test_with_one_param_no_return:
        #Test whether the run-single-test function correctly handles a test function with one parameter and no return value.
        #Success Case: The run-single-test function should conclude that the one-param-no-return function
        #              is working properly when it returns nothing.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(one_param_no_return,(0,),(),test_lib.ASSERT_EQUAL,
                                             "function with one parameter and no return value"),
                                 expected_output=(True,),
                                 test_desc="run-single-test function on test function with one parameter and no "
                                           + "return value (success case)")
        #Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output from
        #           one-param-no-return does not match the actual output.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(one_param_no_return,(0,),(True,),test_lib.ASSERT_EQUAL,
                                             "function with one parameter and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with one parameter and no "
                                          + "return value (fail case)")
        #Fail Case: Make sure that the run-single-test function raises an Assertion error if the one-param-no-return
        #           function raises an unexpected error (which we trigger by not passing the required parameter).
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(one_param_no_return,(),(True,),test_lib.ASSERT_EQUAL,
                                             "function with one parameter and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with one parameter and no "
                                           + "return value (fail case)")
    if test_with_two_param_no_return:
        #Test whether the run-single-test function correctly handles a test function with two parameters and no return value.
        #Success Case: The run-single-test function should conclude that the two-param-no-return function
        #              is working properly when it returns nothing.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(two_param_no_return,(0,0),(),test_lib.ASSERT_EQUAL,
                                             "function with two parameters and no return value"),
                                 expected_output=(True,),
                                 test_desc="run-single-test function on test function with two parameters and no "
                                           + "return value (success case)")
        # Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output from
        #            two-param-no-return does not match the actual output.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(two_param_no_return,(0,0),(True,),test_lib.ASSERT_EQUAL,
                                             "function with two parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with two parameters and no "
                                           + "return value (fail case)")
        # Fail Case: Make sure that the run-single-test function raises an Assertion error if the two-param-no-return
        #            function itself raises an unexpected error (which we trigger by passing too many input arguments).
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(two_param_no_return, (0, 0, 0), (), test_lib.ASSERT_EQUAL,
                                             "function with two parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with two parameters and no "
                                           + "return value (fail case)")
    if test_with_no_param_one_return:
        # Test whether the run-single-test function correctly handles a test function with no parameters and one
        # return value.
        # Success Case: The run-single-test function should conclude that the no-param-one-return function
        #               is working properly when it returns the default integer constant.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_one_return, (), (DEFAULT_INT,), test_lib.ASSERT_EQUAL,
                                             "function with no parameters and one return value"),
                                 expected_output=(True,),
                                 test_desc="run-single-test function on test function with no parameters and one return value "
                                           + "(success case)")
        # Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output from
        #            no-param-one-return does not match the actual output (expects nothing, receives default return
        #            value).
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_one_return, (), (), test_lib.ASSERT_EQUAL,
                                             "function with no parameters and one return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with no parameters and one "
                                           + "return value (fail case)")
        # Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output from
        #            no-param-one-return does not match the actual output (expects one value, receives another).
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_one_return, (), (DEFAULT_INT+1,), test_lib.ASSERT_EQUAL,
                                             "function with no parameters and one return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with no parameters and one "
                                           + "return value (fail case)")
        # Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output from
        #            no-param-one-return does not match the actual output (expects two outputs, receives only one).
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_one_return, (), (DEFAULT_RETURN_VAL, DEFAULT_RETURN_VAL),
                                             test_lib.ASSERT_EQUAL, "function with no parameters and one return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with no parameters and one "
                                           + "return value (fail case)")
    if test_with_no_param_two_return:
        # Test whether the run-single-test function correctly handles a test function with no parameters and two
        # return values.
        # Success Case: The run-single-test function should conclude that the no-param-two-return function
        #               is working properly when it returns the default integer constant and the next integer value.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_two_return, (), (DEFAULT_INT, DEFAULT_INT+1), test_lib.ASSERT_EQUAL,
                                             "function with no parameters and two integer return values"),
                                 expected_output=(True,),
                                 test_desc="run-single-test function on test function with no parameters and two "
                                           "return values (success case)")
        # Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output only
        #            includes the first return value.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_two_return, (), (DEFAULT_INT,), test_lib.ASSERT_EQUAL,
                                             "function with no parameters and two return values"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with no parameters and two "
                                           + " integer return values (fail case)")
        # Fail Case: Make sure that the run-single-test function raises an Assertion error if the first return value
        #            is correct but the second is not.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_two_return, (), (DEFAULT_INT, DEFAULT_INT + 2), test_lib.ASSERT_EQUAL,
                                             "function with no parameters and two return values"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with no parameters and two "
                                           + " integer return values (fail case)")
        # Fail Case: Make sure that the run-single-test function raises an Assertion error if a third return value
        #            is expected.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_two_return, (), (DEFAULT_INT, DEFAULT_INT + 1, DEFAULT_INT + 2),
                                             test_lib.ASSERT_EQUAL,
                                             "function with no parameters and two return values"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with no parameters and two "
                                           + " integer return values (fail case)")

# Test the run-func-tests function from the test helper package.
if test_run_func_tests:
    print("TESTING RUN_FUNC_TESTS FUNCTION")
    if test_with_no_param_no_return:
        # Test whether the run-func-tests function correctly handles a test function with no parameters and no return values.
        # Success Case: The run-func-tests function should conclude that the no-param-no-return function
        #              is working properly when it returns nothing.
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(no_param_no_return, [IOPair((),())], test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(True,),
                                 test_desc="run-func-tests function on test function with no parameters and no return value (success case)")
        # Fail Case: Make sure that the run-func_tests function raises an Assertion error if the expected output from
        #            no-param-one-return does not match the actual output (expects something, receives nothing).
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(no_param_no_return, [IOPair((), (True,))], test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-func-tests function on test function with no parameters and no return value (fail case)")
        # Fail Case: Make sure that the run-func-tests function raises an Assertion error if the no-param-no-return
        #            function itself raises an unexpected error (which we trigger by passing too many input arguments).
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(no_param_no_return, [IOPair((DEFAULT_INT,), ())], test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-func-tests function on test function with no parameters and no return value (fail case)")
        # Mixed Success/Fail Case: Make sure that the run-func-tests function raises an Assertion error if the second
        #                         test fails after the first test is successful.
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(no_param_no_return, [IOPair((), ()),
                                                                  IOPair((),(0,))], test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-func-tests function on test function with no parameters and no return "
                                           +"value (mixed success/fail case)")
    if test_with_one_param_no_return:
        # Test whether the run-func-test function correctly handles a test function with no parameters and no return values.
        # Success Case: The run-single-test function should conclude that the no-param-no-return function
        #              is working properly when it returns nothing.
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(one_param_no_return, [IOPair((DEFAULT_INT,), ())], test_lib.ASSERT_EQUAL,
                                             "function with one parameter and no return value"),
                                 expected_output=(True,),
                                 test_desc="run-func-tests function on test function with one parameter and no return value (success case)")
        # Fail Case: Make sure that the run-func_tests function raises an Assertion error if the expected output from
        #            one-param-one-return does not match the actual output (expects something, receives nothing).
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(one_param_no_return, [IOPair((DEFAULT_INT,), (True,))], test_lib.ASSERT_EQUAL,
                                             "function with one parameter and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-func-tests function on test function with one parameter and no return value (fail case)")
        # Fail Case: Make sure that the run-func-tests function raises an Assertion error if the no-param-no-return
        #            function itself raises an unexpected error (which we trigger by not passing a required input argument).
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(no_param_no_return, [IOPair((), ())], test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-func-tests function on test function with one parameter and no return value (fail case)")
        # Mixed Success/Fail Case: Make sure that the run-func-tests function raises an Assertion error if a second
        #                          test fails after the first test is successful.
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(one_param_no_return, [IOPair((DEFAULT_INT,), ()),
                                                                  IOPair((), (True,))], test_lib.ASSERT_EQUAL,
                                             "function with one parameter and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-func-tests function on test function with one parameter and no return "
                                           + "value (mixed success/fail case)")

def always_true_no_param():
    return True

#test_lib.test_bool_func(always_true_no_param,true_inputs=[()],test_desc="always true function with no parameters")

def always_false_no_param():
    return False

#test_lib.test_bool_func(always_false_no_param,false_inputs=[()],test_desc="always false function with no parameters")

def test_func_always_false(test_int1=0, test_int2=0, test_bool1=True, test_bool2=False, test_str1="", test_str2=""):
    return False

def test_func_is_int(test_input=0):
    return type(test_input) is int

def test_func_is_int_type_error_if_false(test_input=0):
    is_int = type(test_input) is int
    if not is_int:
        raise TypeError(f"{test_input} is not an integer")
    return is_int

# test_lib.test_bool_func(test_func_is_int_type_error_if_false, true_inputs=[],
#                         false_inputs=[(1.0,), (-1.0,), (10000.0,), (-10000.0,), ("",), ("int",), (True,),
#                                       (False,)],
#                         test_desc="is int function with TypeError if false", error_if_false=True, error_type=TypeError)


# class Test(TestCase):
#     def test_test_bool_func(self):
#         # test_lib.test_bool_func(self, test_func_always_true, true_inputs=[(),(1,),(1,2),(1,2,True,False),
#         #                                                                   (1,2,True,False,"A","ab")],
#         #                         test_desc="always true function")
#         # test_lib.test_bool_func(self, test_func_always_false, false_inputs=[(),(1,),(1,2),(1,2,True,False),
#         #                                                                   (1,2,True,False,"A","ab")],
#         #                         test_desc="always false function")
#         # test_lib.test_bool_func(self, test_func_is_int, true_inputs=[(),(1,),(-1,),(10000,),(-10000,)],
#         #                         false_inputs=[(1.0,),(-1.0,),(10000.0,),(-10000.0,),("",),("int",),(True,),(False,)],
#         #                         test_desc="is int function")
#         test_lib.test_bool_func(self, test_func_is_int_type_error_if_false, true_inputs=[(), (1,), (-1,), (10000,), (-10000,)],
#                                 false_inputs=[(1.0,), (-1.0,), (10000.0,), (-10000.0,), ("",), ("int",), (True,),
#                                               (False,)],
#                                 test_desc="is int function with TypeError if false", error_if_false=True, error_type=TypeError)
#         test = 0
