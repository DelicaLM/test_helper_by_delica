"""
This module provides functions to help users easily create and run unit tests for their Python software.
"""

# Import the IOPair class to more easily create and pass input-output pairs for tests.
from test_helper_by_delica.IOPair import IOPair

# Import the time library to measure test runtimes.
import time

# Constants for assertion types (i.e., methods by which we determine whether a test was successful)
# that the user can select for their tests.
ASSERT_EQUAL = "assert_equal"
"""str: Constant string label for the assertion type that checks whether test outputs are equal
to the expected outputs."""
ASSERT_LESS = "assert_less_than"
"""str: Constant string label for the assertion type that checks whether test outputs are less than
expected output values."""
ASSERT_LIST_ELEMENTS_LESS = "assert_list_elements_less_than"
"""str: Constant string label for the assertion type that checks whether all values in an output list are less than
a specified value."""
ASSERT_LESS_OR_EQUAL = "assert_less_or_equal"
"""str: Constant string label for the assertion type that checks whether test outputs are less than or equal
to the expected outputs."""
ASSERT_LIST_ELEMENTS_LESS_OR_EQUAL = "assert_list_elements_less_than_or_equal"
"""str: Constant string label for the assertion type that checks whether all values in an output list are less than
or equal to a specified value."""
ASSERT_GREATER = "assert_greater_than"
"""str: Constant string label for the assertion type that checks whether test outputs are greater
than the expected output values."""
ASSERT_LIST_ELEMENTS_GREATER = "assert_list_elements_greater_than"
"""str: Constant string label for the assertion type that checks whether all values in an output list are greater than
a specified value."""
ASSERT_GREATER_OR_EQUAL = "assert_greater_or_equal"
"""str: Constant string label for the assertion type that checks whether test outputs are greater than or equal
to the expected outputs."""
ASSERT_LIST_ELEMENTS_GREATER_OR_EQUAL = "assert_list_elements_greater_than_or_equal"
"""str: Constant string label for the assertion type that checks whether all values in an output list are greater than
or equal to a specified value."""
ASSERT_RAISES = "assert_raises"
"""str: Constant string label for the assertion type that checks whether the test function raises an Exception."""
ASSERT_IN_SET = "assert_in_set"
"""str: Constant string label for the assertion type that checks whether test outputs are elements in a provided set."""
ASSERT_LIST_ELEMENTS_IN_SET = "assert_list_elements_in_set"
"""str: Constant string label for the assertion type that checks whether all elements in an output list are present 
in a provided set."""
ASSERT_TYPE = "assert_output_is_type"
"""str: Constant string label for the assertion type that checks whether test outputs have the expected data types."""
ASSERT_LIST_ELEMENTS_TYPE = "assert_list_elements_type"
"""str: Constant string label for the assertion type that checks whether all elements in an output list have the 
expected data types."""
ASSERT_TYPES = [ASSERT_EQUAL, ASSERT_LESS, ASSERT_LIST_ELEMENTS_LESS, ASSERT_LESS_OR_EQUAL,
                ASSERT_LIST_ELEMENTS_LESS_OR_EQUAL, ASSERT_GREATER, ASSERT_LIST_ELEMENTS_GREATER,
                ASSERT_GREATER_OR_EQUAL, ASSERT_RAISES, ASSERT_IN_SET, ASSERT_LIST_ELEMENTS_IN_SET, ASSERT_TYPE,
                ASSERT_LIST_ELEMENTS_TYPE,]
"""list: List of all the assertion types that are currently supported in this module."""

MAX_PRINTED_LIST_ITEMS = 5

def make_tuple_str(input_tuple):
    """Creates a more readable string representation of a tuple.

    Parameters
    ----------
    input_tuple : tuple | any
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
        if isinstance(item, list):
            # If the item is a list, we iterate over each of its elements to make sure that
            # we add their correct string forms to the list (otherwise str(list) can give the
            # obj.__repr__() string instead of obj.__str__()).
            result += "["
            index = 0
            while index < len(item) and index < MAX_PRINTED_LIST_ITEMS:
                curr_item = item[index]
                result += str(curr_item)
                if index < len(item) - 1:
                    result += ", "
                index += 1
            if len(item) > MAX_PRINTED_LIST_ITEMS:
                result += "..., " + str(item[-1])
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
        to check if one is greater than a certain value and if the other is less than a different value, then you can
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
    # Assume, by default, that the tuples do not match according to the comparison method.
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
            elif comp_type == ASSERT_LIST_ELEMENTS_LESS:
                all_outputs_correct &= type(output_val_1) == list
                if all_outputs_correct:
                    index = 0
                    while index < len(output_val_1) and all_outputs_correct:
                        element = output_val_1[index]
                        all_outputs_correct &= element < output_val_2
                        index += 1
            elif comp_type == ASSERT_LESS_OR_EQUAL:
                all_outputs_correct &= output_val_1 <= output_val_2
            elif comp_type == ASSERT_LIST_ELEMENTS_LESS_OR_EQUAL:
                all_outputs_correct &= type(output_val_1) == list
                if all_outputs_correct:
                    index = 0
                    while index < len(output_val_1) and all_outputs_correct:
                        element = output_val_1[index]
                        all_outputs_correct &= element <= output_val_2
                        index += 1
            elif comp_type == ASSERT_GREATER:
                all_outputs_correct &= output_val_1 > output_val_2
            elif comp_type == ASSERT_LIST_ELEMENTS_GREATER:
                all_outputs_correct &= type(output_val_1) == list
                if all_outputs_correct:
                    index = 0
                    while index < len(output_val_1) and all_outputs_correct:
                        element = output_val_1[index]
                        all_outputs_correct &= element > output_val_2
                        index += 1
            elif comp_type == ASSERT_GREATER_OR_EQUAL:
                all_outputs_correct &= output_val_1 >= output_val_2
            elif comp_type == ASSERT_LIST_ELEMENTS_GREATER_OR_EQUAL:
                all_outputs_correct &= type(output_val_1) == list
                if all_outputs_correct:
                    index = 0
                    while index < len(output_val_1) and all_outputs_correct:
                        element = output_val_1[index]
                        all_outputs_correct &= element >= output_val_2
                        index += 1
            elif comp_type == ASSERT_IN_SET:
                all_outputs_correct &= output_val_1 in output_val_2
            elif comp_type == ASSERT_LIST_ELEMENTS_IN_SET:
                all_outputs_correct &= type(output_val_1) == list
                if all_outputs_correct:
                    index = 0
                    while index < len(output_val_1) and all_outputs_correct:
                        element = output_val_1[index]
                        all_outputs_correct &= element in output_val_2
                        index += 1
            elif comp_type == ASSERT_TYPE:
                if isinstance(output_val_2, type) and isinstance(output_val_1, type):
                    all_outputs_correct &= output_val_1 == output_val_2
                elif isinstance(output_val_2, type):
                    all_outputs_correct &= isinstance(output_val_1, output_val_2)
                elif isinstance(output_val_1, type):
                    all_outputs_correct &= isinstance(output_val_2, output_val_1)
                else:
                    all_outputs_correct &= type(output_val_1) == type(output_val_2)
            elif comp_type == ASSERT_LIST_ELEMENTS_TYPE:
                all_outputs_correct &= type(output_val_1) == list
                if all_outputs_correct:
                    index = 0
                    while index < len(output_val_1) and all_outputs_correct:
                        element = output_val_1[index]
                        all_outputs_correct &= type(element) == output_val_2
                        index += 1
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
        is less than a different value, then you can provide the list [ASSERT_GREATER, ASSERT_LESS] for this parameter.
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
        Boolean flag indicating whether we should include the test's input in the error message that is displayed if
        the test fails. Consider setting this parameter to False if your test description already includes the test
        input.

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
        raise TypeError(f"{test_func} is not callable. Please provide a callable test function.")
    # Make sure that the assertion type(s) are valid.
    if type(assert_type) != list:
        if assert_type not in ASSERT_TYPES:
            raise ValueError(f"{assert_type} is not a valid assertion type. Please select one of the following options:"
                             + f" {ASSERT_TYPES}")
    else:
        for compare_type in assert_type:
            if compare_type not in ASSERT_TYPES:
                raise ValueError(f"{compare_type} is not a valid assertion type. Please select one of the following "
                                + f"options: {', '.join(ASSERT_TYPES)}")
    # Make sure that the test description is a string.
    if type(test_desc) != str:
        raise TypeError(f"{test_desc} is not a string. Test description must be a string.")
    # Make sure that the flag for whether we should raise an AssertionError if the test fails is a boolean.
    if type(raise_error_on_fail) != bool:
        raise TypeError(f"{raise_error_on_fail} is not a boolean. Raise error on failure flag must be a boolean "
                        + f"(True or False).")
    # Make sure that the flag for whether we should print a new line after the test is a boolean.
    if type(add_new_line) != bool:
        raise TypeError(f"{add_new_line} is not a boolean. Add new line flag must be a boolean (True or False).")
    # Make sure that the flag for whether we should include the inputs when we print the test results is a boolean.
    if type(include_input_in_error_msg) != bool:
        raise TypeError(f"{include_input_in_error_msg} is not a boolean. Include input in error message flag must be a "
                        + f"boolean (True or False).")
    # If the expected output is a tuple of length one, we extract the single element (particularly useful when the
    # expected output is an Exception type).
    if type(expected_output) == tuple:
        if len(expected_output) == 1:
            expected_output = expected_output[0]
    # Start by printing the test description.
    print("Testing " + test_desc)
    # Make string representations of the input and expected output tuples.
    input_string = make_tuple_str(test_input)
    expected_output_string = make_tuple_str(expected_output)
    # Determine if the expected output is an Exception.
    should_raise_error = False
    error_type = None
    try:
        should_raise_error = expected_output is Exception or issubclass(expected_output, Exception)
    except TypeError: # issubclass will trigger an error if expected_output is not a class
        pass # If issubclass raises a TypeError, the expected output is not a class and, therefore, cannot be an
             # Exception type. Since the should raise error flag is False by default, we don't need to perform
             # any additional work in this exception block.
    if should_raise_error: # if the expected output is an Exception
        error_type = expected_output # get the type of Exception that the user expects
    # Assume that the test fails by default.
    test_succeeded = False
    test_output = None
    # Keep track of how long the test takes.
    test_runtime= 0.0
    start_time = time.time()
    end_time = time.time()
    # We need to run the test a bit differently depending on whether or not the expected output is an Exception.
    if should_raise_error: #if the expected output is an Exception
        assert error_type is not None
        assert error_type is Exception or issubclass(error_type, Exception)
        try:
            test_output = test_func(*test_input)
            test_output_string = make_tuple_str(test_output)
            end_time = time.time()
        except error_type as e:
            # In this case, the test succeeds if we end up in the except branch for the
            # error type defined by expected output.
            end_time = time.time()
            test_succeeded = True
            test_output = error_type
            test_output_string = error_type.__name__
            print(f"ERROR MESSAGE: {e}")
    else: #if the expected output is not an Exception
        # In this scenario, the test fails if any Exceptions are raised.
        unwanted_error_raised = False
        unwanted_error_type = None
        test_output = None
        start_time = time.time()
        try:
            test_output = test_func(*test_input)
            test_output_string = make_tuple_str(test_output)
            end_time = time.time()
        except Exception as e:
            # If an unexpected error is raised, we print the information out to the user.
            end_time = time.time()
            unwanted_error_raised = True
            unwanted_error_type = type(e)
            test_output = unwanted_error_type
            test_output_string = unwanted_error_type.__name__
            test_succeeded = False
            unwanted_error_type_name = unwanted_error_type.__name__
            print(f"TEST FUNCTION RAISED UNEXPECTED {unwanted_error_type_name}\n   ERROR MESSAGE: {e}")
        if not unwanted_error_raised:
            # If no Exceptions were raised, we need to check whether the actual output matches the expected output.
            test_succeeded = compare_output_tuples(test_output, expected_output, compare_type=assert_type)
    # Record the time at the end of the test.
    end_time = time.time()
    # Print the test results to the user.
    if not test_succeeded:
        fail_msg = f"FAIL: {test_desc.upper()} FAILED "
        if include_input_in_error_msg:
            fail_msg += f"WITH INPUT = {input_string} "
        if assert_type == ASSERT_TYPE:
            fail_msg += f"(EXPECTED OUTPUT TYPE = {expected_output.__name__}, ACTUAL_OUTPUT = {test_output_string})"
        elif assert_type == ASSERT_LIST_ELEMENTS_TYPE:
            fail_msg += f"(EXPECTED OUTPUT TYPE = list[{expected_output.__name__}], ACTUAL_OUTPUT = {test_output_string})"
        elif assert_type == ASSERT_LIST_ELEMENTS_IN_SET:
            fail_msg += f"(EXPECTED OUTPUT VALUES = {str(expected_output)}, ACTUAL_OUTPUT = {test_output_string})"
        else:
            fail_msg += f"(EXPECTED OUTPUT = {expected_output_string}, ACTUAL_OUTPUT = {test_output_string})"
        # Check if we should raise an Assertion Error to alert the user that their test failed.
        if raise_error_on_fail:
            raise AssertionError(fail_msg)
        else:
            print(fail_msg)
    else:
        print(f"SUCCESS: input={input_string}\n         output={test_output_string}")
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
        Raised if any of the tests fail and raise_error_on_fail is set to True.
    """
    # Make sure that the test function is callable.
    if not callable(test_func):
        raise TypeError(f"{test_func} is not callable. Test function must be callable.")
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
            raise TypeError(f"{correct_io_pairs} is not a list. You must provide a list of IOPair objects "
                            + f"(one for each test).")
        for io_pair in correct_io_pairs:
            if not isinstance(io_pair, IOPair):
                raise TypeError(f"{io_pair} is not an IOPair. Every item in the input-output pairs list must be an "
                                + f"IOPair object.")
    # Make sure that the test description is a string.
    if type(test_desc) != str:
        raise TypeError(f"{test_desc} is not a string. Test description must be a string.")
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
        # Get the input and output for the test
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
        # Run the test.
        is_success = run_single_test(test_func, test_input, expected_output, assert_type=assert_type,
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
    # Make a string showing all the failed test numbers.
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
    # Print the summary of test failures (will print "0 FAILED TESTS" if all tests succeeded).
    print(failed_tests_line)
    return all_tests_succeeded


def clean_input_tuple_list(input_list):
    """Turns a list of function inputs into a list of tuples (the format expected by many of the testing functions).
    Caution: This function will turn each element of the input list into its own tuple, which might not be the
    behaviour that you desire. In order to prevent this type of parsing error, please consider adding the appropriate
    tuple parentheses to your inputs before using this function.

    Parameters
    ----------
    input_list : list
        The input list

    Returns
    -------
    result : list
        The correctly formatted list of input tuples.
    """
    result = []
    if input_list is not None:
        result = input_list
        if not isinstance(input_list, list):
            result = [input_list]
        for i in range(len(result)):
            if not isinstance(result[i], tuple):
                result[i] = (result[i],)
    return result

def make_io_pairs_from_input_list(input_list, expected_output):
    """Makes a list of IOPairs objects from a list of input tuples that should all yield the same expected output.

    Parameters
    ----------
    input_list : list
        The list of input tuples.
    expected_output : tuple | any
        The expected output tuple that should occur for all of the input tuples in input_list. If the user does not pass
        a tuple for this parameter, the function will convert the provided output value into a tuple with a single
        element.

    Returns
    -------
    io_pairs : list[IOPair]
        The list of IOPairs generated from the input tuple list and the expected output.
    """
    io_pairs = []
    output_tuple = ()
    if expected_output is not None:
        output_tuple = expected_output
        if not isinstance(expected_output, tuple):
            output_tuple = (expected_output,)
    input_list = clean_input_tuple_list(input_list)
    for input_tuple in input_list:
        new_io_pair = IOPair(input_tuple, output_tuple)
        io_pairs.append(new_io_pair)
    return io_pairs

def test_bool_func(test_func, true_inputs=None, false_inputs=None, test_desc="", error_if_false=False,
                   error_if_false_type=Exception, raise_error_on_fail=True, type_error_inputs=None,
                   value_error_inputs=None, assert_error_inputs =None,):
    """Runs a sequence of tests for a function that returns a boolean value.

    Parameters
    ----------
    test_func : function
        The boolean function that should be tested.
    true_inputs : list[tuple] | list[any],  optional, default=None
        List of input tuples that should cause the test function to return True.
    false_inputs : list[tuple] | list[any], optional, default=None
        List of input tuples that should cause the test function to return False.
    test_desc : str, optional, default=""
        A description of the tests that should be printed to stdout.
    error_if_false : bool, optional, default=False
        Boolean flag for whether the function should raise an error when the condition it evaluates is False.
    error_if_false_type : type, optional, default=Exception
        The type of exception that should be raised for False results (if error_if_false is True).
    raise_error_on_fail : bool, optional, default=True
        A boolean flag indicating whether an AssertionError should be raised if a test fails.
    type_error_inputs : list[tuple] | list[any], optional, default=None
        List of input tuples that should cause the test function to raise a TypeError.
    value_error_inputs : list[tuple] | list[any], optional, default=None
        List of input tuples that should cause the test function to raise a ValueError.
    assert_error_inputs : list[tuple] | list[any], optional, default=None
        List of input tuples that should cause the test function to raise an AssertionError.

    Returns
    -------
    bool
        Returns True if all tests were successful, False otherwise.

    Raises
    ______
    AssertionError
        Raised if raise_error_on_fail is True and any of the tests fail (stdout messages allow the user to easily
        determine which test case failed).
    """
    # Make sure that the test function is callable.
    if not callable(test_func):
        raise TypeError(f"{test_func} is not callable. Test function must be callable.")
    # Ensure that the input lists are lists of tuples
    true_inputs = clean_input_tuple_list(true_inputs)
    false_inputs = clean_input_tuple_list(false_inputs)
    type_error_inputs = clean_input_tuple_list(type_error_inputs)
    value_error_inputs = clean_input_tuple_list(value_error_inputs)
    assert_error_inputs = clean_input_tuple_list(assert_error_inputs)
    # Make sure that the error if false flag is a boolean.
    if type(error_if_false) != bool:
        raise TypeError(f"{error_if_false} is not a boolean. Error if false flag must be a boolean (True or False).")
    if error_if_false:
        # If the test function should raise an exception for False outputs, we need to check whether the user provided
        # a valid exception type.
        is_exception = True
        try:
            is_exception = error_if_false_type is Exception or issubclass(error_if_false_type, Exception)
        except TypeError: # issubclass raises a Type Error if error_type is not a class
            is_exception = False # If error_type is not a class, it can't be an Exception type.
        if not is_exception:
            raise TypeError(f"{error_if_false_type} is not a valid Exception type. The error type must be a valid "
                            + f"exception type in Python (e.g., TypeError, ValueError, etc.).")
    # Make sure that the user provided a string for the test description.
    if type(test_desc) != str:
        raise TypeError("Test description must be a string.")
    # Convert the input tuples into IOPair objects.
    io_pairs = []
    true_io_pairs = make_io_pairs_from_input_list(true_inputs, True)
    io_pairs.extend(true_io_pairs)
    false_result = False
    if error_if_false:
        false_result = error_if_false_type
    false_io_pairs = make_io_pairs_from_input_list(false_inputs, false_result)
    io_pairs.extend(false_io_pairs)
    type_error_io_pairs = make_io_pairs_from_input_list(type_error_inputs, TypeError)
    io_pairs.extend(type_error_io_pairs)
    value_error_io_pairs = make_io_pairs_from_input_list(value_error_inputs, ValueError)
    io_pairs.extend(value_error_io_pairs)
    assert_error_io_pairs = make_io_pairs_from_input_list(assert_error_inputs, AssertionError)
    io_pairs.extend(assert_error_io_pairs)
    # Run the boolean function tests.
    all_tests_succeeded = run_func_tests(test_func, io_pairs, assert_type=ASSERT_EQUAL, test_desc=test_desc,
                                         raise_error_on_fail=raise_error_on_fail)
    return all_tests_succeeded

