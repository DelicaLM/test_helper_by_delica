"""
This module provides functions to help users easily create and run unit tests for their Python software.

Functions
---------
make_tuple_str(input_tuple)
    Returns a string representation of an input tuple (improves readability of test outputs).
compare_output_tuples(output_tuple1, output_tuple2, compare_type=ASSERT_EQUAL)
    Returns True if two tuples match based on a user-specified comparison (e.g., "==", "<", ">", etc.) and False
    otherwise (used to check whether tested functions yield the correct output).
run_single_test(test_func, test_input=(), expected_output=(), assert_type=ASSERT_EQUAL, test_desc="",
                add_new_line=True,include_input_in_error_msg=True):
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

from test_helper_by_delica.IOPair import IOPair

ASSERT_EQUAL = "assert_equal"
ASSERT_RAISES = "assert_raises"
ASSERT_TYPES = [ASSERT_EQUAL, ASSERT_RAISES]

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
    else: # if the parameter is a tuple
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
    """Checks whether two tuples agree with each other based on a specified comparison type (e.g., "==", "<", ">", etc.).

    Parameters
    ----------
    output_tuple1 : tuple | any
        The first tuple in comparison. If it is not passed as a tuple, this function will convert it to a tuple with a
        single element.
    output_tuple2 : tuple | any
        The second tuple in comparison. If it is not passed as a tuple, this function will convert it to a tuple with a
        single element.
    compare_type : str
        The name of the comparison type that should be used (must be a value from the ASSERT_TYPES list at the start
        of this file (test_helper_funcs.py)).

    Returns
    -------
    bool
        Returns True if the tuples match based on the comparison type and False if they do not.
    """
    if type(output_tuple1) != tuple:
        output_tuple1 = (output_tuple1,)
    if type(output_tuple2) != tuple:
        output_tuple2 = (output_tuple2,)
    result = False
    if compare_type == ASSERT_EQUAL:
        result = output_tuple1 == output_tuple2
        if output_tuple1 == () or output_tuple1 == (None,):
            result = output_tuple2  == () or output_tuple2 == (None,)
    return result


def run_single_test(test_func, test_input=(), expected_output=(), assert_type=ASSERT_EQUAL, test_desc="",
                    add_new_line=True,include_input_in_error_msg=True):
    """Runs a single unit test for a given function.

    Parameters
    ----------
    test_func : function
        The function that should be tested.
    test_input : tuple, optional, default=()
        The input tuple that will be passed to the test function.
    expected_output : tuple, optional, default=()
        The expected output that should be returned by the test function.
    assert_type : str, optional, default=ASSERT_EQUAL
        The name of the assertion type (e.g., ASSERT_EQUAL, ASSERT_RAISES) that should be used to check whether the
        test was successful. This parameter must be a value from the ASSERT_TYPES constants list at the top of
        this file (test_helper_funcs.py).
    test_desc : str, default=""
        A description of the test that should be printed to stdout.
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
        Raised if the test fails.
    """
    assert callable(test_func)
    if type(expected_output) == tuple:
        if len(expected_output) == 1:
            expected_output = expected_output[0]
    print("Testing " + test_desc)
    input_string = make_tuple_str(test_input)
    expected_output_string = make_tuple_str(expected_output)
    use_assert_raises = False
    error_type = None
    use_assert_raises = False
    try:
        use_assert_raises = expected_output is Exception or issubclass(expected_output, Exception)
    except TypeError:
        pass
    if use_assert_raises:
        error_type = expected_output
    test_succeeded = False

    if use_assert_raises:
        assert error_type is not None
        assert error_type is Exception or issubclass(error_type, Exception)
        try:
            test_func(*test_input)
        except error_type as e:
            test_succeeded = True
            print(f"ERROR MESSAGE: {e}")
    else:
        unwanted_error_raised = False
        unwanted_error_type = None
        test_output = None
        try:
            test_output = test_func(*test_input)
        except Exception as e:
            unwanted_error_raised = True
            unwanted_error_type = type(e)
            test_output = unwanted_error_type
            test_succeeded = False
            unwanted_error_type_name = unwanted_error_type.__name__
            print(f"TEST FUNCTION RAISED UNEXPECTED {unwanted_error_type_name}\n   ERROR MESSAGE: {e}")

        if not unwanted_error_raised:
            output_is_correct = compare_output_tuples(test_output, expected_output, compare_type=assert_type)
            test_succeeded = output_is_correct
        if not test_succeeded:
            fail_msg = f"{test_desc.upper()} FAILED "
            if include_input_in_error_msg:
                fail_msg += f"WITH INPUT = {input_string} "
            fail_msg += f"(EXPECTED OUTPUT = {expected_output}, ACTUAL_OUTPUT = {test_output})"
            raise AssertionError(fail_msg)
    if test_succeeded:
        print(f"SUCCESS: input={input_string}\n         output={expected_output_string}")
    if add_new_line:
        print("")
    return test_succeeded


def run_func_tests(test_func, correct_io_pairs, assert_type=ASSERT_EQUAL, test_desc=""):
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
    assert_type : str, optional, default=ASSERT_EQUAL
        The name of the assertion type (e.g., ASSERT_EQUAL, ASSERT_RAISES) that should be used to check whether the
        test was successful. This parameter must be a value from the ASSERT_TYPES constants list at the top of
        this file (test_helper_funcs.py).
    test_desc : str, optional default="",
        A description of the tests that should be printed to stdout.
    Returns
    -------
    bool all_tests_succeeded
        A boolean flag indicating whether all of the tests were successful.

    Raises
    ______
    AssertionError
        Raised if any of the tests fail (stdout messages allow the user to easily determine which test case failed).
    """
    assert callable(test_func), "Test function must be callable."
    assert assert_type in ASSERT_TYPES, "Assertion type must be a value from the ASSERT_TYPES constants list."
    if isinstance(correct_io_pairs, IOPair):
        correct_io_pairs = [correct_io_pairs]
    else:
        assert type(correct_io_pairs) == list, "Input-output pairs must be passed as a list of IO_Pair objects."
        for io_pair in correct_io_pairs:
            assert isinstance(io_pair, IOPair), "Every item in the input-output pairs list must be an IO_Pair object."
    assert type(test_desc) == str, "Test description must be a string."
    print("TESTING " + test_desc.upper())
    num_tests = len(correct_io_pairs)
    num_succeeded = 0
    num_failed = 0
    failed_test_nums = []
    test_num = 1
    for io_pair in correct_io_pairs:
        curr_assert_type = assert_type
        assert isinstance(io_pair, IOPair)
        test_input = io_pair.input_tuple
        assert type(test_input) == tuple, "Test input must be a tuple."
        expected_output = io_pair.output_tuple
        assert type(expected_output) == tuple, "Expected test output must be a tuple."
        if len(expected_output) > 0:
            try:
                if expected_output[0] is Exception or issubclass(expected_output[0], Exception):
                    curr_assert_type = ASSERT_RAISES
            except TypeError:
                curr_assert_type = assert_type
        print(f"Test #{test_num} of {num_tests}")
        is_success = run_single_test(test_func, test_input, expected_output, assert_type=curr_assert_type,
                                     test_desc=f"{test_func.__name__} function for input " + str(test_input),
                                     add_new_line=False, include_input_in_error_msg=False)
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


def test_bool_func(test_func, true_inputs=None, false_inputs=None, error_if_false=False, error_type=Exception,
                   test_desc="", success_desc=""):
    """Runs a set of unittest tests for a function that returns a boolean value.

    Parameters
    ----------
    test_func : function
        The boolean function that should be tested.
    true_inputs : list[tuple], optional, default=None
        List of input tuples that should cause the test function to return True.
    false_inputs : list[tuple], optional, default=None
        List of input tuples that should cause the test function to return False.
    error_if_false : bool, default=False
        Boolean flag for whether the function should raise an error when the condition it evaluates is False.
    error_type : type, default=Exception
        The type of exception that should be raised for False results.
    test_desc : str, default="",
        A description of the tests that should be printed to stdout.

    Returns
    -------
    None
    (Test results are printed to stdout.)

    Raises
    ______
    AssertionError
        Raised if any of the tests fail (stdout messages allow the user to easily determine which test case failed).

    """
    assert callable(test_func)
    if true_inputs is None:
        true_inputs = []
    else:
        assert type(true_inputs) == list
    if false_inputs is None:
        false_inputs = []
    else:
        assert type(false_inputs) == list
    assert type(false_inputs) == list
    assert type(error_if_false) == bool
    assert issubclass(error_type, Exception)
    assert type(test_desc) == str
    assert type(success_desc) == str
    io_pairs = []
    for true_input in true_inputs:
        if type(true_input) != tuple:
            true_input = (true_input,)
        new_io_pair = IOPair(true_input, (True,))
        io_pairs.append(new_io_pair)
    false_result = False
    if error_if_false:
        false_result = error_type
    for false_input in false_inputs:
        if type(false_input) != tuple:
            false_input = (false_input,)
        new_io_pair = IOPair(false_input, (false_result,))
        io_pairs.append(new_io_pair)
    run_func_tests(test_func, io_pairs, assert_type=ASSERT_EQUAL, test_desc=test_desc)

