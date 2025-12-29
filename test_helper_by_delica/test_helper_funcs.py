from unittest import TestCase
from test_helper_by_delica.IOPair import IOPair

ASSERT_EQUAL = "assert_equal"
ASSERT_RAISES = "assert_raises"
ASSERT_NAMES = [ASSERT_EQUAL, ASSERT_RAISES]

def get_assert_func(unittest_obj, assert_name):
    if assert_name not in ASSERT_NAMES:
        raise ValueError(f"VALUE ERROR IN GET_ASSERT_FUNC: {assert_name} is not a valid unittest assert function.")
    assert assert_name in ASSERT_NAMES
    assert_func = None
    if assert_name == ASSERT_EQUAL:
        assert_func = unittest_obj.assertEqual
    elif assert_name == ASSERT_RAISES:
        assert_func = unittest_obj.assertRaises
    assert assert_func is not None
    return assert_func



class TestClass(TestCase):
    pass
    # def return_self(self):
    #     return self

def create_unittest_obj():
    """Creates and returns an instance of an unittest TestCase"""
    return TestClass()#.return_self()

def run_single_test(test_func, unittest_obj, assert_func, test_input=(), expected_output=(),
                    test_desc=""):
    """Runs a single test using an unittest TestCase object.

    Parameters
    ----------
    test_func : function
        The function that should be tested.
    unittest_obj : TestCase
        The unittest TestCase object that should be used to run the test.
    assert_func : function
        The unittest assertion function that should be used to verify the result of the test.
    test_input : tuple, default=()
        The input tuple that will be passed to the test function.
    expected_output : tuple, default=()
        The expected output that should be returned by the test function.
    test_desc : str, default=""
        A description of the test that should be printed to stdout.

    Returns
    -------
    None

    Raises
    ______
    AssertionError
        Raised if the test fails.
    """
    assert isinstance(unittest_obj, TestCase)
    assert callable(assert_func)
    # test = getattr(TestCase, assert_func.__name__)
    # assert callable(getattr(unittest_obj, assert_func.__name__))
    assert callable(test_func)
    if type(expected_output) == tuple:
        if len(expected_output) == 1:
            expected_output = expected_output[0]
    print("Testing " + test_desc)
    input_string = str(test_input)
    expected_output_string = str(expected_output)
    use_assert_raises = False
    error_type = None
    use_assert_raises = issubclass(expected_output, Exception)
    if use_assert_raises:
        error_type = expected_output
    test_succeeded = False

    if use_assert_raises:
        assert error_type is not None
        # error_type = Exception
        # if len(expected_output) > 0:
        #     error_type = expected_output[0]
        assert error_type is Exception or issubclass(error_type, Exception)
        with unittest_obj.assertRaises(error_type) as context_manager:
            test_func(*test_input)
        raised_exception = context_manager.exception
        if raised_exception is not None:
            print(f"ERROR MESSAGE: {str(raised_exception)}")
            test_succeeded = isinstance(raised_exception, error_type)
    else:
        test_output = test_func(*test_input)
        if hasattr(test_output, "__len__"):
            assert len(test_output) == len(expected_output)
        fail_msg = (f"{test_desc.upper()} FAILED WITH INPUT = {input_string}, EXPECTED_OUTPUT = {expected_output_string},"
                    + f" ACTUAL_OUTPUT = {test_output}")
        if type(test_output) is tuple:
            try:
                assert_func(*test_output, *expected_output, msg=fail_msg)
                test_succeeded = True
            except AssertionError as e:
                print(f"FAILURE: {fail_msg}")
        else:
            try:
                assert_func(test_output, expected_output, msg=fail_msg)
                test_succeeded = True
            except AssertionError as e:
                print(f"FAILURE: {fail_msg}")

        # assert_func(test_output, *expected_output)
    if test_succeeded:
        print(f"SUCCESS: input={input_string} -> output={expected_output_string}")
    return test_succeeded


def run_func_tests(test_func, unittest_obj, correct_io_pairs, assert_func_name=ASSERT_EQUAL, test_desc=""):
    """Runs a set of unittest tests for a specified function.

    Parameters
    ----------
    test_func : function
        The function that should be tested.
    unittest_obj : TestCase
        The unittest TestCase object that should be used to run the tests.
    correct_io_pairs : list[IOPair]
        List of the input-output pairs that should occur if the test function is working properly. The number of
        input-output pairs determines the number of tests that will be run. For each input-output pair, this function
        will pass the input to the function that we are testing. It will then use the requested assertion function to
        check whether the actual output matches the expected output from the input-output pair.
    assert_func_name : str
        The string name (from the constants at the top of test_helper_funcs.py) that corresponds to the unittest
        assertion function we should use to check whether each test is successful.
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
    assert isinstance(unittest_obj, TestCase), "Unittest object must be an instance of TestCase."
    assert callable(test_func), "Test function must be callable."
    assert_func = get_assert_func(unittest_obj, assert_func_name),
    assert assert_func is not None, "Assertion function must not be None."
    if type(assert_func) is tuple:
        assert_func = assert_func[0]
    assert callable(assert_func), "Assertion function must be callable."
    if isinstance(correct_io_pairs, IOPair):
        correct_io_pairs = [correct_io_pairs]
    else:
        assert type(correct_io_pairs) == list, "Input-output pairs must be passed as a list of IO_Pair objects."
        for io_pair in correct_io_pairs:
            assert isinstance(io_pair, IOPair), "Every item in the input-output pairs list must be an instance of IO_Pair object."
    assert type(test_desc) == str, "Test description must be a string."
    print("TESTING " + test_desc.upper())
    # io_pairs = []
    # for io_pair in input_output_pairs:
    #     if io_pair != ():
    #         io_pairs.append(io_pair)
    num_tests = len(correct_io_pairs)
    num_succeeded = 0
    num_failed = 0
    failed_test_nums = []
    test_num = 1
    for io_pair in correct_io_pairs:
        curr_assert_func = assert_func
        assert isinstance(io_pair, IOPair)
        test_input = io_pair.input_tuple
        assert type(test_input) == tuple, "Test input must be a tuple."
        expected_output = io_pair.output_tuple
        assert type(expected_output) == tuple, "Expected test output must be a tuple."
        if len(expected_output) > 0:
            if issubclass(expected_output[0], Exception):
                curr_assert_func = unittest_obj.assertRaises
        print(f"Test #{test_num} of {num_tests}")
        is_success = run_single_test(test_func, unittest_obj, curr_assert_func, test_input, expected_output,
                        f"{test_func.__name__} function for input " + str(test_input))
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
    print(f"{num_failed} FAILED TESTS ({failed_test_nums_str})")


def test_bool_func(test_func, unittest_obj, true_inputs=None, false_inputs=None, error_if_false=False, error_type=Exception,
                   test_desc="", success_desc=""):
    """Runs a set of unittest tests for a function that returns a boolean value.

    Parameters
    ----------
    test_func : function
        The boolean function that should be tested.
    unittest_obj : TestCase
        The unittest TestCase object that should be used to run the tests.
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

    Raises
    ______
    AssertionError
        Raised if any of the tests fail (stdout messages allow the user to easily determine which test case failed).

    """
    assert isinstance(unittest_obj, TestCase)
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
    # test_inputs = true_inputs.copy()
    # test_inputs.extend(false_inputs)
    # expected_outputs = [(True)] * len(true_inputs)
    # false_output = False
    # if error_if_false:
    #     false_output = error_type
    # expected_outputs.extend([(false_output)] * len(false_inputs))
    # num_tests = len(io_pairs)
    # if num_tests > 0:
    #     io_pairs = [()]*num_tests
    #     io_index = 0
    #     while io_index < num_tests:
    #         test_input = test_inputs[io_index]
    #         expected_output = expected_outputs[io_index]
    #         io_pairs[io_index] = (test_input, expected_output)
    #         io_index += 1
    run_func_tests(test_func, unittest_obj, io_pairs,assert_func_name=ASSERT_EQUAL, test_desc=test_desc)


    # test_num = 1
    # num_tests = len(true_inputs) + len(false_inputs)
    # for true_input in true_inputs:
    #     assert type(true_input) == tuple
    #     print(f"Test #{test_num} of {num_tests}")
    #     run_single_test(unittest_obj, assert_func, test_func, true_input, (True), f"{test_func.__name__} function for input "
    #                     + str(true_input), success_desc)
    #     test_num += 1
    # for false_input in false_inputs:
    #     assert type(false_input) == tuple
    #     print(f"Test #{test_num} of {num_tests}")
    #     if error_if_false:
    #         assert_func = unittest_obj.assertRaises
    #     run_single_test(unittest_obj, assert_func, test_func, false_input, TypeError,
    #                     f"{test_func.__name__} function for input "
    #                     + str(false_input), success_desc)
    # test_num += 1

# def make_io_pair(test_input, expected_output):
#     test_input_tuple = test_input
#     if type(test_input) != tuple:
#         test_input_tuple = (test_input,)
#     expected_output_tuple = expected_output
#     if type(expected_output) != tuple:
#         expected_output_tuple = (expected_output,)
#     return (test_input_tuple, expected_output_tuple)
#
# def make_io_pairs(test_inputs, expected_outputs):
#     result = []
#     assert