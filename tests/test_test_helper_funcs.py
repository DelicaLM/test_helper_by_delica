"""Script to test the functions in the test helper package (test_helper_funcs.py)."""

import src.test_helper_funcs as test_lib
from src.IOPair import IOPair

DEFAULT_INT = 0
"int : Default integer value that should be returned by a function (makes it easier to standardize tests)."
DEFAULT_RETURN_VAL = DEFAULT_INT
"int : Default return value returned by functions in this test suite."

test_run_single_test = False
"bool : Boolean flag for whether or not to run the tests for the run_single_test function."
test_run_func_tests = False
"bool : Boolean flag for whether or not to run the tests for the run_func_tests function."
test_test_bool_func = True
"bool : Boolean flag for whether or not to run the tests for the test_bool_func function."

test_with_no_param_no_return = False
"bool : Boolean flag for whether to test the testing library on a function with no parameters and no outputs."
test_with_one_param_no_return = False
"bool : Boolean flag for whether to test the testing library on a function with one parameter and no outputs."
test_with_two_param_no_return = False
"bool : Boolean flag for whether to test the testing library on a function with two parameters and no outputs."
test_with_no_param_one_return = False
"bool : Boolean flag for whether to test the testing library on a function with no parameters and one return value."
test_with_no_param_two_return = False
"bool : Boolean flag for whether to test the testing library on a function with no parameters and two return values."
test_with_always_true = False
"bool : Boolean flag for whether to test the testing library on a function than always returns True."
test_with_always_false = False
"bool : Boolean flag for whether to test the testing library on a function than always returns False."
test_with_is_even = False
"bool : Boolean flag for whether to test the testing library on a function than outputs whether an integer is even."
test_with_list_has_val_with_type_errors = True
"bool : Boolean flag for whether to test the library on a function that checks if a list contains a certain value."


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

def one_param_one_return(int_val):
    """Function with one integer parameter and one integer return value.

    Parameters
    ----------
    int_val : int
        An integer parameter.

    Returns
    -------
    int
        Returns the sum of one and the integer parameter (int_val + 1).
    """
    return int_val + 1

def two_param_two_return(int_val, str_val):
    """Function with two parameters and two return values.

    Parameters
    ----------
    int_val : int
        An integer parameter.
    str_val : str
        A string parameter.
    Returns
    -------
    int
        The sum of one and the integer parameter (int_val + 1).
    str
        The concatenation of the string parameter and "a".
    """
    return int_val + 1, str_val + "a"

def always_true():
    """Returns True."""
    return True

def always_false():
    """Returns False."""
    return False

def is_even(int_val):
    """Returns True if the input parameter is an even integer.

    Parameters
    ----------
    int_val : int
        The integer value that we need to check for evenness.
    Returns
    -------
    bool
        A boolean indicating if the input parameter is an even integer.
    """
    return type(int_val) == int and int_val % 2 == 0

def list_has_val_with_type_errors(list_to_search, int_val):
    """Returns True if the list contains the specified integer value.

    Parameters
    ----------
    list_to_search : list
        The list in which we should look for the value.
    int_val : int
        The integer value that we will try to find in the list.

    Returns
    -------
    bool
        A boolean indicating if the list contains the specified integer value.
    """
    if type(list_to_search) != list:
        raise TypeError("list_to_search must be of type list")
    if type(int_val) != int:
        raise TypeError("int_val must be of type int")
    return int_val in list_to_search


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
        # Test whether the run-func-test function correctly handles a test function with one parameter and no output.
        # Success Case: The run-single-test function should conclude that the no-param-no-return function
        #              is working properly when it returns nothing.
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(one_param_no_return, [IOPair((DEFAULT_INT,), ())],
                                             test_lib.ASSERT_EQUAL,"function with one parameter and no return value"),
                                 expected_output=(True,),
                                 test_desc="run-func-tests function on test function with one parameter and no return "
                                           + "value (success case)")
        # Fail Case: Make sure that the run-func_tests function raises an Assertion error if the expected output from
        #            one-param-one-return does not match the actual output (expects something, receives nothing).
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(one_param_no_return,
                                             [IOPair((DEFAULT_INT,), (True,))],
                                             test_lib.ASSERT_EQUAL,"function with one parameter and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-func-tests function on test function with one parameter and no return "
                                           "value (fail case)")
        # Fail Case: Make sure that the run-func-tests function raises an Assertion error if the required input
        #            argument is missing.
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(no_param_no_return, [IOPair((), ())], test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-func-tests function on test function with one parameter and no return "
                                           + "value (fail case)")
        # Mixed Success/Fail Case: Make sure that the run-func-tests function raises an Assertion error if a second
        #                          test fails after the first test is successful.
        test_lib.run_single_test(test_lib.run_func_tests,
                                 test_input=(one_param_no_return, [IOPair((DEFAULT_INT,), ()),
                                                                  IOPair((), (True,))],
                                             test_lib.ASSERT_EQUAL, "function with one parameter and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-func-tests function on test function with one parameter and no return "
                                           + "value (mixed success/fail case)")

if test_test_bool_func:
    if test_with_always_true:
        # Test whether the test-bool-func function correctly handles a test function that always returns True.
        # Success Case: The test-bool-func function should conclude that the always-true function is working properly
        #               when it returns True.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(always_true, [()], [], "always true function"),
                                 expected_output=(True,),
                                 test_desc="test-bool-func on test function that always returns True (success case)")
        # Fail Case: Make sure that test-bool-func function raises an AssertionError if the actual output (True) does
        #            not match the expected output (False) and the raise_error_on_fail flag is True.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(always_true, [], [()], "always true function"),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that always returns True (fail case)")
        # Fail Case: Make sure that test-bool-func function returns False instead of an AssertionError if a test fails
        #            and the raise_error_on_fail flag is True.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(always_true, [], [()], "always true function", False, None, False),
                                 expected_output=(False,),
                                 test_desc="test-bool-func on test function that always returns True (fail case)")
        # Fail Case: Make sure that test-bool-func function returns an Assertion error if a second test fails after
        #            the first one passed.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(always_true, [()], [()], "always true function"),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that always returns True (fail case)")
    if test_with_always_false:
        # Test whether the test-bool-func function correctly handles a test function that always returns False.
        # Success Case: The test-bool-func function should conclude that the always-false function is working properly
        #               when it returns False.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(always_false, [], [()], "always false function"),
                                 expected_output=(True,),
                                 test_desc="test-bool-func on test function that always returns False (success case)")
        # Fail Case: Make sure that test-bool-func function raises an AssertionError if the actual output (False) does
        #            not match the expected output (True) and the raise_error_on_fail flag is True.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(always_false, [()], [], "always false function"),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that always returns False (fail case)")
        # Fail Case: Make sure that test-bool-func function returns False instead of an AssertionError if a test fails
        #            and the raise_error_on_fail flag is True.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(always_false, [()], [], "always false function", False, None, False),
                                 expected_output=(False,),
                                 test_desc="test-bool-func on test function that always returns False (fail case)")
        # Fail Case: Make sure that test-bool-func function returns an Assertion error if a second test fails after
        #            the first one passed.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(always_false, [()], [()], "always false function"),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that always returns False (fail case)")
    if test_with_is_even:
        # Test whether the test-bool-func function correctly handles a test function that checks if an integer is even.
        # Success Case: The test-bool-func function should conclude that the is-even function is working properly
        #               when it returns True for even integers and False for odd integers.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(is_even, [2, 4, 6, 8, 10, 100], [-1, 1, 3, 101], "is even function"),
                                 expected_output=(True,),
                                 test_desc="test-bool-func on test function that determines whether an integer is even "
                                           + "(success case)")
        # Fail Case: Make sure that the test-bool-func raises an error if the expected output is True when the actual
        #            output is False and the raise_error_on_fail flag is True.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(is_even, [1], [], "is even function"),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that determines whether an integer is even "
                                           + "(fail case)")
        # Fail Case: Make sure that the test-bool-func raises an error if the expected output is False when the actual
        #            output is True and the raise_error_on_fail flag is True.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(is_even, [], [2], "is even function"),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that determines whether an integer is even "
                                           + "(fail case)")
        # Fail Case: Make sure that the test-bool-func returns False and does not raise an error if a test fails and
        #            the raise_error_on_fail flag is False.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(is_even, [], [2], "is even function", False, None, False),
                                 expected_output=(False,),
                                 test_desc="test-bool-func on test function that determines whether an integer is even "
                                           + "(fail case)")
        # Fail Case: Make sure that the test-bool-func raises an Assertion Error if one of many tests fail and the
        #            raise_error_on_fail flag is True.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(is_even, [2, 4, 5, 6], [1, 3, 5], "is even function"),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that determines whether an integer is even "
                                           + "(fail case)")
        # Fail Case: Make sure that the test-bool-func raises an AssertionError if multiple tests fail and the
        #            raise_error_on_fail flag is True.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(is_even, [2, 4, 5, 6, 7], [1, 3, 5, 4, 6], "is even function"),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that determines whether an integer is even "
                                           + "(fail case)")
        # Fail Case: Make sure that the test-bool-func returns False and does not raise an error if one of many tests
        #            fail and the raise_error_on_fail flag is False.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(is_even, [2,4,5,6], [1,3,5], "is even function", False, None, False),
                                 expected_output=(False,),
                                 test_desc="test-bool-func on test function that determines whether an integer is even "
                                           + "(fail case)")
        # Fail Case: Make sure that the test-bool-func returns False and does not raise an error if multiple tests
        #            fail and the raise_error_on_fail flag is False.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(is_even, [2, 4, 5, 6, 7], [1, 3, 5, 4, 6], "is even function", False, None,
                                             False),
                                 expected_output=(False,),
                                 test_desc="test-bool-func on test function that determines whether an integer is even "
                                           + "(fail case)")
    if test_with_list_has_val_with_type_errors:
        # Test whether the test-bool-func function correctly handles a test function that checks if an integer value
        # is in a list and raises TypeErrors if the two parameters are not, respectively, a list and an integer.
        # Success Case: The test-bool-func function should conclude that the value in list function is working properly
        #               when it returns True when a list contains the target value and False when it does not.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(list_has_val_with_type_errors,
                                             [([1],1),([1,2],1),([1,2,3,4,5],5)], [([],1), ([1],2), ([1,2,3], 4)],
                                             "list has val with type errors function", False, Exception, True,
                                             [([1,2], 1.0), ([],1.0), (1,[])]),
                                 expected_output=(True,),
                                 test_desc="test-bool-func on test function that determines whether a list contains a "
                                           + "particular integer value with type errors\nif the parameters are "
                                           + "incorrect (i.e., not a list and an integer) (success case)")
        # Fail Case: The test-bool-func function should conclude that the value in list function is not working properly
        #            if we expect a True result for a list that does not contain the target value.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(list_has_val_with_type_errors,
                                             [([1], 2)],[],
                                             "list has val with type errors function", False, Exception, True,
                                             []),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that determines whether a list contains a "
                                           + "particular integer value with type errors\nif the parameters are "
                                           + "incorrect (i.e., not a list and an integer) (fail case)")
        # Fail Case: The test-bool-func function should conclude that the value in list function is not working properly
        #            if we expect a False result for a list that does contain the target value.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(list_has_val_with_type_errors,
                                             [], [([1], 1)],
                                             "list has val with type errors function", False, Exception, True,
                                             []),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that determines whether a list contains a "
                                           + "particular integer value with type errors\nif the parameters are "
                                           + "incorrect (i.e., not a list and an integer) (fail case)")
        # Fail Case: The test-bool-func function should conclude that the value in list function is not working properly
        #            if we expect the function to raise a TypeError and it does not.
        test_lib.run_single_test(test_lib.test_bool_func,
                                 test_input=(list_has_val_with_type_errors,
                                             [], [],
                                             "list has val with type errors function", False, Exception, True,
                                             [([1,2], 1)]),
                                 expected_output=(AssertionError,),
                                 test_desc="test-bool-func on test function that determines whether a list contains a "
                                           + "particular integer value with type errors\nif the parameters are "
                                           + "incorrect (i.e., not a list and an integer) (fail case)")


