"""
This module provides functions to help users easily create and run unit tests for their Python software.

Functions
---------
make_tuple_str(input_tuple)
    Returns a string representation of an input tuple (improves readability of test outputs).

compare_output_tuples(output_tuple1, output_tuple2, compare_type=ASSERT_EQUAL)
    Returns True if two tuples match based on a user-specified comparison (e.g., "==", "<", ">", etc.) and False
    otherwise (used to check whether tested functions yield the correct output).

run_single_test(test_func, test_input=(), expected_output=(), assert_type=ASSERT_EQUAL, test_desc="", add_new_line=True,
    include_input_in_error_msg=True)
    Runs a single test of a function. Returns True if all the tests succeed and raises an AssertionError if
    any of the tests fail.

run_func_tests(test_func, correct_io_pairs, assert_type=ASSERT_EQUAL, test_desc="")
    Runs one or more tests for a function. Returns True if all the tests succeed and raises an AssertionError if
    any of the tests fail.

test_bool_func(test_func, true_inputs=None, false_inputs=None, error_if_false=False, error_type=Exception,
    test_desc="", success_desc="")
    Runs one or more tests for a boolean function. Returns True if all the tests succeed and raises an AssertionError if
    any of the tests fail.

"""

# Import the IOPair class to more easily create and pass input-output pairs for tests
from src.IOPair import IOPair

# Import the time library to measure test runtimes.
import time

# Constants for assertion types (i.e., methods in which we determine whether a test was successful) that the user
# can use for their tests.
ASSERT_EQUAL = "assert_equal" # use if test outputs should be equal to the expected outputs
ASSERT_LESS = "assert_less_than" # use if the actual outputs should be less than the expected output values
ASSERT_LESS_OR_EQUAL = "assert_less_or_equal" # use if the actual outputs should be <= to the expected output values
ASSERT_GREATER = "assert_greater_than" # use if the actual outputs should be more than the expected output values
ASSERT_GREATER_OR_EQUAL = "assert_greater_or_equal" # use if the actual outputs should be >= to the expected outputs
ASSERT_RAISES = "assert_raises" # use if the tested function should raise an Exception
ASSERT_TYPE = "assert_output_is_type" # use if the test should verify whether the output is of a certain type
ASSERT_TYPES = [ASSERT_EQUAL, ASSERT_LESS, ASSERT_LESS_OR_EQUAL, ASSERT_GREATER, ASSERT_GREATER_OR_EQUAL,
                ASSERT_RAISES, ASSERT_TYPE]

def make_tuple_str(input_tuple):
    """Creates a more readable string representation of a tuple.

    Parameters
    ----------
    input_tuple : tuple
        The tuple that we must convert into a string. (If you do not pass a tuple for this parameter, this function will
        create the appropriate tuple for your input before generating the string output.)

    Returns
    -------
    str
        The string representation of the tuple.
    """
    # Start the string with an open parenthesis.
    result = "("
    # Check if the user actually passed a tuple.
    is_tuple = isinstance(input_tuple, tuple)
    # Find all the tuple items that we need to print.
    input_items = []
    if not is_tuple:
        # If the parameter is not a tuple, we only have one element.
        input_items.append(input_tuple)
    else: # If the parameter is a tuple
        for item in input_tuple: # iterate over all the elements in the tuple
            input_items.append(item)
    # Add each tuple item to the string.
    for item in input_items:
        if isinstance(item, list): # If the item is a list, we iterate over each of its elements to make sure that
                                   # we add their correct string forms to the list (otherwise str(list) can give the
                                   # obj.__repr__() string instead of obj.__str__()).
            result += "["
            for list_item in item:
                result += str(list_item)
                if list_item != item[-1]:
                    result += ", "
            result += "]"
        elif callable(item) or isinstance(item, type): # If the item is a class or function, make sure that we only
                                                       # print its name.
            result += item.__name__
        else:
            result += str(item)
        if item != input_items[-1] or len(input_items) == 1:
            result += ", "
    result += ")"
    # Return the string that we created for the tuple.
    return result

def compare_output_tuples(output_tuple1, output_tuple2, compare_type=ASSERT_EQUAL):
    """Checks whether two tuples agree with each other based on a specified comparison type ("==", "<", ">", etc.).

    Parameters
    ----------
    output_tuple1 : tuple | any
        The first tuple in the comparison. If it is not passed as a tuple, this function will convert it to a tuple with
        a single element.
    output_tuple2 : tuple | any
        The second tuple in the comparison. If it is not passed as a tuple, this function will convert it to a tuple
        with a single element.
    compare_type : str | list[str], optional, default ASSERT_EQUAL
        The name of the comparison type that should be used (must be a value from the ASSERT_TYPES list at the start
        of this file (test_helper_funcs.py)). If you want your outputs to be checked with different assertion types,
        you can instead provide a list of comparison methods. For example, if you have two integer outputs and you want
        to check if one is greater than a certain value and if the other is less than another value, then you can
        provide the list [ASSERT_GREATER, ASSERT_LESS] for this parameter. If your list is shorter than the number of
        outputs, the last comparison type in the list will be used for the remaining output values.

    Returns
    -------
    bool
        Returns True if the tuples match based on the comparison type and False if they do not.
    """
    # Convert the outputs to tuples if they are not already in that form.
    if type(output_tuple1) != tuple:
        output_tuple1 = (output_tuple1,)
    if type(output_tuple2) != tuple:
        output_tuple2 = (output_tuple2,)
    result = False
    # Make a list of the comparison types that should be used for the outputs
    compare_types = []
    # If the user passes a single string for the comparison type, we just need to add it to our list.
    if type(compare_type) == str:
        if compare_type not in ASSERT_TYPES:
            raise ValueError(f"The comparison type '{compare_type}' is not supported. Please choose from the following "
                             + f"options: {', '.join(ASSERT_TYPES)}")
        compare_types.append(compare_type)
    elif type(compare_type) == list: # If the user provides a list of comparison types, we need to check whether each
                                     # element is a valid comparison type and then add it to the list.
        for assert_type in compare_types:
            if assert_type not in ASSERT_TYPES:
                raise ValueError(f"The comparison type '{assert_type}' is not supported. Please choose from the "
                                 f"following options: {', '.join(ASSERT_TYPES)}")
            compare_types.append(assert_type)
    # If the number of comparison types is less than the number of outputs, we use the last comparison type in the
    # list for the remaining output values.
    if len(compare_types) < len(output_tuple1):
        assert len(compare_types) > 0
        last_compare_type = compare_types[-1]
        while len(compare_types) < len(output_tuple1):
            compare_types.append(last_compare_type)
    # Check if the tuples have the same lengths (if not, we instantly know that the comparison result will be false).
    if len(output_tuple1) == len(output_tuple2):
        # Make sure that we have the correct number of comparison types.
        assert len(compare_types) == len(output_tuple1)
        # Start by assuming that the outputs are all correct.
        all_outputs_correct = True
        # Iterate over the output values.
        for comp_num in range(len(output_tuple1)):
            # Use the comparison type that the user has requested for this output.
            comp_type = compare_types[comp_num]
            output_val_1 = output_tuple1[comp_num]
            output_val_2 = output_tuple2[comp_num]
            if comp_type == ASSERT_EQUAL:
                all_outputs_correct &= output_val_1 == output_val_2
            elif comp_type == ASSERT_LESS:
                all_outputs_correct &= output_val_1 < output_val_2
            elif comp_type == ASSERT_LESS_OR_EQUAL:
                all_outputs_correct &= output_val_1 <= output_val_2
            elif comp_type == ASSERT_GREATER:
                all_outputs_correct &= output_val_1 > output_val_2
            elif comp_type == ASSERT_GREATER_OR_EQUAL:
                all_outputs_correct &= output_val_1 >= output_val_2
            elif comp_type == ASSERT_TYPE:
                all_outputs_correct &= type(output_val_1) == type(output_val_2)
        # Only return True if all of the outputs were correct based on their comparison type.
        result = all_outputs_correct
    return result


def run_single_test(test_func, test_input=(), expected_output=(), assert_type=ASSERT_EQUAL, test_desc="",
                    raise_error_on_fail=True, add_new_line=True, include_input_in_error_msg=True):
    """Runs a single unit test for a given function.

    Parameters
    ----------
    test_func : function
        The function that should be tested.
    test_input : tuple, optional, default=()
        The input tuple that will be passed to the test function.
    expected_output : tuple, optional, default=()
        The expected output that should be returned by the test function.
    assert_type : str | list[str], optional, default ASSERT_EQUAL
        The name of the assertion type that should be used for checking whether a test was successful (must be a value
        from the ASSERT_TYPES list at the start of this file (test_helper_funcs.py)). If you want your outputs to be
        checked with different assertion types, you can instead provide a list of comparison methods. For example,
        if you have two integer outputs and you want to check if one is greater than a certain value and if the other
        is less than another value, then you can provide the list [ASSERT_GREATER, ASSERT_LESS] for this parameter.
        If your list is shorter than the number of outputs, the last comparison type in the list will be used for the
        remaining output values.
    test_desc : str, optional, default=""
        A description of the test that should be printed to stdout.
    raise_error_on_fail : bool, optional, default=True
        A boolean flag indicating whether an AssertionError should be raised if the test fails.
    add_new_line : bool, optional, default=True
        Boolean flag indicating whether we should add a blank line after we finish printing the test results to stdout
        (useful for readability).
    include_input_in_error_msg : bool, optional, default=True
        Boolean flag indicating whether we should include the test's input in the error message that is displayed
        if the test fails (included to prevent the input from being printed twice if the test description already
        includes the input).

    Returns
    -------
    bool
     A boolean flag indicating whether the test was successful.

    Raises
    ______
    AssertionError
        Raised if the test fails and the raise_error_on_fail flag is set to True.
    """
    # Make sure that the test function is callable.
    if not callable(test_func):
        raise TypeError("Test function must be callable.")
    # Make sure that the assertion type(s) are valid.
    if type(assert_type) != list:
        if assert_type not in ASSERT_TYPES:
            raise ValueError(f"{assert_type} is not a valid assertion type. Please select one of the following options:"
                             + f" {ASSERT_TYPES}")
    else:
        for compare_type in assert_type:
            if compare_type not in ASSERT_TYPES:
                raise ValueError("{compare_type} is not a valid assertion type. Please select one of the following "
                                + f"options: {ASSERT_TYPES}")
    # Make sure that the test description is a string.
    if type(test_desc) != str:
        raise TypeError(f"Test description must be a string.")
    # Make sure that the flag for whether we should raise an AssertionError if the test fails is a boolean.
    if type(raise_error_on_fail) != bool:
        raise TypeError(f"Raise error on failure flag must be a boolean (True or False).")
    # Make sure that the flag for whether we should print a new line after the test is a boolean.
    if type(add_new_line) != bool:
        raise TypeError(f"Add new line flag must be a boolean (True or False).")
    # Make sure that the flag for whether we should include the inputs when we print the test results is a boolean
    if type(include_input_in_error_msg) != bool:
        raise TypeError(f"Include input in error message flag must be a boolean (True or False).")
    # If the expected output is a tuple of length one, we extract the single element (particularly useful when the
    # expected output is an Exception type).
    if type(expected_output) == tuple:
        if len(expected_output) == 1:
            expected_output = expected_output[0]
    # Start by printing the test description.
    print("Testing " + test_desc)
    # Make string representations of the input and expected output tuples
    input_string = make_tuple_str(test_input)
    expected_output_string = make_tuple_str(expected_output)
    # Determine if the expected output is an Exception.
    should_raise_error = False
    error_type = None
    try:
        should_raise_error = expected_output is Exception or issubclass(expected_output, Exception)
    except TypeError:
        pass
    if should_raise_error:
        error_type = expected_output
    # Assume that the test fails by default.
    test_succeeded = False
    test_output = None
    # Keep track of how long the test takes.
    test_runtime= 0.0
    start_time = 0.0
    end_time = 0.0
    # We need to run the test a bit differently depending on whether the expected output is an Exception.
    if should_raise_error: #if the expected output is an Exception
        assert error_type is not None
        assert error_type is Exception or issubclass(error_type, Exception)
        try:
            start_time = time.time()
            test_output = test_func(*test_input)
            end_time = time.time()
        except error_type as e:
            # In this case, the test succeeds if we end up in the except branch for the
            # error type defined by expected output.
            test_succeeded = True
            test_output = error_type
            end_time = time.time()
            print(f"ERROR MESSAGE: {e}")
    else: #if the expected output is not an Exception
        # In this scenario, the test fails if any Exceptions are raised.
        unwanted_error_raised = False
        unwanted_error_type = None
        test_output = None
        start_time = time.time()
        try:
            test_output = test_func(*test_input)
        except Exception as e:
            # If an unexpected error is raised, we print the information out to the user.
            unwanted_error_raised = True
            unwanted_error_type = type(e)
            test_output = unwanted_error_type
            test_succeeded = False
            unwanted_error_type_name = unwanted_error_type.__name__
            print(f"TEST FUNCTION RAISED UNEXPECTED {unwanted_error_type_name}\n   ERROR MESSAGE: {e}")
        if not unwanted_error_raised:
            # If no Exceptions were raised, we need to check whether the actual output matches the expected output.
            test_succeeded = compare_output_tuples(test_output, expected_output, compare_type=assert_type)
    end_time = time.time()
    if not test_succeeded:
        fail_msg = f"FAIL: {test_desc.upper()} FAILED "
        if include_input_in_error_msg:
            fail_msg += f"WITH INPUT = {input_string} "
        fail_msg += f"(EXPECTED OUTPUT = {expected_output}, ACTUAL_OUTPUT = {test_output})"
        if raise_error_on_fail:
            raise AssertionError(fail_msg)
        else:
            print(fail_msg)
    else:
        print(f"SUCCESS: input={input_string}\n         output={expected_output_string}")
        test_runtime = end_time - start_time
        print(f"TEST RUNTIME: {test_runtime:.20f} seconds")
    if add_new_line:
        print("")
    return test_succeeded


def run_func_tests(test_func, correct_io_pairs, assert_type=ASSERT_EQUAL, test_desc="", raise_error_on_fail=True):
    """Runs a set of unit tests for a specified function.

    Parameters
    ----------
    test_func : function
        The function that should be tested.
    correct_io_pairs : list[IOPair]
        List of the input-output pairs that should occur if the test function is working properly. The number of
        input-output pairs determines the number of tests that will be run. For each input-output pair, this function
        will pass the input to the function that we are testing. It will then use the requested assertion function to
        check whether the actual output matches the expected output from the input-output pair.
    assert_type : str | list[str], default ASSERT_EQUAL
        The name of the assertion type that should be used for checking whether a test was successful (must be a value
        from the ASSERT_TYPES list at the start of this file (test_helper_funcs.py)). If you want your outputs to be
        checked with different assertion types, you can instead provide a list of comparison methods. For example,
        if you have two integer outputs and you want to check if one is greater than a certain value and if the other
        is less than another value, then you can provide the list [ASSERT_GREATER, ASSERT_LESS] for this parameter.
        If your list is shorter than the number of outputs, the last comparison type in the list will be used for the
        remaining output values.
    test_desc : str, optional, default="",
        A description of the tests that should be printed to stdout.
    raise_error_on_fail : bool, optional, default=True
        A boolean flag indicating whether an AssertionError should be raised if a test fails.
    Returns
    -------
    all_tests_succeeded : bool
        A boolean flag indicating whether all of the tests were successful.

    Raises
    ______
    AssertionError
        Raised if any of the tests fail (stdout messages allow the user to easily determine which test case failed).
    """
    # Make sure that the test function is callable.
    if not callable(test_func):
        raise TypeError("Test function must be callable.")
    # Make sure that the user chose a valid assertion type.
    if assert_type not in ASSERT_TYPES:
        raise ValueError(f"{assert_type} is not a valid assertion type. Please select one of the following options: "
                        + f"{ASSERT_TYPES}")
    # If the user passed a single IOPair that is not in a list, we make it the single element in a list of length one.
    if isinstance(correct_io_pairs, IOPair):
        correct_io_pairs = [correct_io_pairs]
    else:
        # If the user did not provide a lone IOPair, we need to make sure that they passed a list of IOPairs.
        if type(correct_io_pairs) != list:
            raise TypeError("You must provide a list of IOPair objects (one for each test).")
        for io_pair in correct_io_pairs:
            if not isinstance(io_pair, IOPair):
                raise TypeError("Every item in the input-output pairs list must be an IOPair object.")
    # Make sure that the test description is a string.
    if type(test_desc) != str:
        raise TypeError("Test description must be a string.")
    # Start by printing the test description
    print("TESTING " + test_desc.upper())
    # Get the total number of tests that should be run.
    num_tests = len(correct_io_pairs)
    # Keep track of how many tests succeeded and how many failed.
    num_succeeded = 0
    num_failed = 0
    # Keep track of which tests failed.
    failed_test_nums = []
    # Keep track of the current test number.
    test_num = 1
    for io_pair in correct_io_pairs:
        curr_assert_type = assert_type
        assert isinstance(io_pair, IOPair)
        test_input = io_pair.input_tuple
        assert type(test_input) == tuple, "Test input must be a tuple."
        expected_output = io_pair.output_tuple
        assert type(expected_output) == tuple, "Expected test output must be a tuple."
        # if len(expected_output) > 0:
        #     try:
        #         if expected_output[0] is Exception or issubclass(expected_output[0], Exception):
        #             curr_assert_type = ASSERT_RAISES
        #     except TypeError:
        #         curr_assert_type = assert_type
        print(f"Test #{test_num} of {num_tests}")
        is_success = run_single_test(test_func, test_input, expected_output, assert_type=curr_assert_type,
                                     test_desc=f"{test_func.__name__} function for input " + str(test_input),
                                     raise_error_on_fail=raise_error_on_fail, add_new_line=False,
                                     include_input_in_error_msg=False)
        test_num += 1
        if is_success:
            num_succeeded += 1
        else:
            num_failed += 1
            failed_test_nums.append(test_num-1)
    print(f"ALL {num_tests} TESTS COMPLETED FOR {test_desc.upper()}")
    print(f"{num_succeeded} SUCCESSFUL TESTS")
    failed_test_nums_str = ""
    for failed_test_num in failed_test_nums:
        failed_test_nums_str += f"#{failed_test_num}"
        if failed_test_num != failed_test_nums[-1]:
            failed_test_nums_str += ", "
    failed_tests_line = f"{num_failed} FAILED TESTS"
    if num_failed > 0:
        failed_tests_line += f" ({failed_test_nums_str})"
    failed_tests_line += "\n"
    all_tests_succeeded = num_succeeded == num_tests
    print(failed_tests_line)
    return all_tests_succeeded


def test_bool_func(test_func, true_inputs=None, false_inputs=None, test_desc="", error_if_false=False,
                   error_type=Exception, raise_error_on_fail=True, type_error_inputs=None, value_error_inputs=None,
                   assert_error_inputs =None,):
    """Runs a sequence of tests for a function that returns a boolean value.

    Parameters
    ----------
    test_func : function
        The boolean function that should be tested.
    true_inputs : list[tuple], optional, default=None
        List of input tuples that should cause the test function to return True.
    false_inputs : list[tuple], optional, default=None
        List of input tuples that should cause the test function to return False.
    test_desc : str, optional, default=""
        A description of the tests that should be printed to stdout.
    error_if_false : bool, optional, default=False
        Boolean flag for whether the function should raise an error when the condition it evaluates is False.
    error_type : type, optional, default=Exception
        The type of exception that should be raised for False results (if error_if_false is True).
    raise_error_on_fail : bool, optional, default=True
        A boolean flag indicating whether an AssertionError should be raised if a test fails.
    type_error_inputs : list[tuple], optional, default=None
        List of input tuples that should cause the test function to raise a TypeError.
    value_error_inputs : list[tuple], optional, default=None
        List of input tuples that should cause the test function to raise a ValueError.
    assert_error_inputs : list[tuple], optional, default=None
        List of input tuples that should cause the test function to raise an AssertionError.

    Returns
    -------
    bool
        Returns True if all tests were successful, False otherwise.

    Raises
    ______
    AssertionError
        Raised if raise_error_on_fail is True and  any of the tests fail (stdout messages allow the user to easily
        determine which test case failed).
    """
    # Make sure that the test function is callable.
    if not callable(test_func):
        raise TypeError("Test function must be callable.")
    # Make sure that the user provided lists (or nothing) for the true and false inputs.
    if true_inputs is None:
        true_inputs = []
    else:
        if type(true_inputs) != list:
            raise TypeError("You need to provide a list of input tuples for the true test cases.")
    if false_inputs is None:
        false_inputs = []
    else:
        if type(false_inputs) != list:
            raise TypeError("You need to provide a list of input tuples for the false test cases.")
    if type_error_inputs is None:
        type_error_inputs = []
    else:
        if type(type_error_inputs) != list:
            raise TypeError("You need to provide a list of input tuples for the TypeError test cases.")
    if value_error_inputs is None:
        value_error_inputs = []
    else:
        if type(value_error_inputs) != list:
            raise TypeError("You need to provide a list of input tuples for the ValueError test cases.")
    if assert_error_inputs is None:
        assert_error_inputs = []
    else:
        if type(assert_error_inputs) != list:
            raise TypeError("You need to provide a list of input tuples for the AssertError test cases.")
    # Make sure that the error if false flag is a boolean.
    if type(error_if_false) != bool:
        raise TypeError("Error if false flag must be a boolean (True or False).")
    if error_if_false:
        # If the test function should raise an exception for False outputs, we need to check whether the user provided
        # a valid exception type.
        is_exception = True
        try:
            is_exception = issubclass(error_type, Exception)
        except TypeError:
            is_exception = False
        if not is_exception:
            raise TypeError("Error type must be a valid exception type in Python (e.g., TypeError, ValueError, etc.).")
    # Make sure that the user provided a string for the test description.
    if type(test_desc) != str:
        raise TypeError("Test description must be a string.")
    # Convert the input tuples into IOPair objects.
    io_pairs = []
    # Make IOPairs for inputs that should yield True.
    for true_input in true_inputs:
        if type(true_input) != tuple:
            true_input = (true_input,)
        new_io_pair = IOPair(true_input, (True,))
        io_pairs.append(new_io_pair)
    # Make IOPairs for inputs that should yield False (or an error).
    false_result = False
    if error_if_false:
        false_result = error_type
    for false_input in false_inputs:
        if type(false_input) != tuple:
            false_input = (false_input,)
        new_io_pair = IOPair(false_input, (false_result,))
        io_pairs.append(new_io_pair)
    # Make IOPairs for inputs that should yield a TypeError.
    for type_error_input in type_error_inputs:
        if type(type_error_input) != tuple:
            type_error_input = (type_error_input,)
        new_io_pair = IOPair(type_error_input, (TypeError,))
        io_pairs.append(new_io_pair)
    # Make IOPairs for inputs that should yield a ValueError.
    for value_error_input in value_error_inputs:
        if type(value_error_input) != tuple:
            value_error_input = (value_error_input,)
        new_io_pair = IOPair(value_error_input, (ValueError,))
        io_pairs.append(new_io_pair)
    # Make IOPairs for inputs that should yield a AssertionError.
    for assert_error_input in assert_error_inputs:
        if type(assert_error_input) != tuple:
            assert_error_input = (assert_error_input,)
        new_io_pair = IOPair(assert_error_input, (AssertionError,))
        io_pairs.append(new_io_pair)
    # Run the boolean function tests.
    all_tests_succeeded = False
    all_tests_succeeded = run_func_tests(test_func, io_pairs, assert_type=ASSERT_EQUAL, test_desc=test_desc,
                                         raise_error_on_fail=raise_error_on_fail)
    return all_tests_succeeded

