"""Script to test the functions in the test data generators module (test_data_generators.py)."""

# Import the test helper module to run the tests.
from test_helper_by_delica.test_helper_funcs import *
# Import the IOPair class.
from test_helper_by_delica.IOPair import IOPair
# Import the data generator functions.
from test_helper_by_delica.test_data_generators import *

# Declare flags for whether each of the tests should be run.
run_all_tests = True
"bool : Boolean flag for whether all tests should be run, regardless of their boolean flags below."

test_get_rand_bool = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_bool function."
test_get_rand_bool_list = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_bool_list function."

test_get_rand_int = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_int function."
test_get_rand_pos_int = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_pos_int function."
test_get_rand_neg_int = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_neg_int function."
test_get_rand_int_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_int_list function."
test_get_rand_pos_int_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_pos_int_list function."
test_get_rand_neg_int_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_neg_int_list function."

test_get_rand_float = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_float function."
test_get_rand_pos_float = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_pos_float function."
test_get_rand_neg_float = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_neg_float function."
test_get_rand_float_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_float_list function."
test_get_rand_pos_float_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_pos_float_list function."
test_get_rand_neg_float_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_neg_float_list function."

test_get_rand_letter_lowercase = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_letter_lowercase function."
test_get_rand_letter_uppercase = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_letter_uppercase function."
test_get_rand_letter_mixedcase = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_letter_mixedcase function."
test_get_rand_letter_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_letter_list function."
test_get_rand_uppercase_letter_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_uppercase_letter_list function."
test_get_rand_lowercase_letter_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_lowercase_letter_list function."

test_get_rand_az_string_lowercase = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_az_string_lowercase function."
test_get_rand_az_string_uppercase = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_az_string_uppercase function."
test_get_rand_az_string_mixedcase = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_az_string_mixedcase function."
test_get_rand_mixedcase_az_string_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_mixedcase_az_string_list function."
test_get_rand_lowercase_az_string_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_lowercase_az_string_list function."
test_get_rand_uppercase_az_string_list = False
"bool : Boolean flag for whether or not to run the tests for the get_rand_uppercase_az_string_list function."

if test_get_rand_bool or run_all_tests:
    # Make sure that get_rand_bool returns a boolean.
    run_func_tests(get_rand_bool, [
        IOPair((),(bool,))
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_bool return type")
    # Make sure that get_rand_bool returns True or False
    # (redundant with the previous test).
    run_func_tests(get_rand_bool, [
        IOPair((), ([True, False],))
    ], assert_type=ASSERT_IN_SET, test_desc="get_rand_bool return value")

if test_get_rand_bool_list or run_all_tests:
    # Make sure that all elements in the get_rand_bool_list output are booleans.
    run_func_tests(get_rand_bool_list, [
        IOPair((1,), (bool,)),
        IOPair((10,), (bool,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_bool_list return type")
    # Make sure that all elements in get_rand_bool_list are True or False
    # (redundant with the previous test).
    run_func_tests(get_rand_bool_list, [
        IOPair((1,), ([True, False],)),
        IOPair((10,), ([True, False],)),
    ], assert_type=ASSERT_LIST_ELEMENTS_IN_SET, test_desc="get_rand_bool_list return values")
    # Make sure that get_rand_bool_list raises errors for incorrect parameters.
    run_func_tests(get_rand_bool_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_bool_list errors for incorrect parameters")

if test_get_rand_int or run_all_tests:
    # Make sure that get_rand_int returns an integer.
    run_func_tests(get_rand_int, [
        IOPair((),(int,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_int return type")

if test_get_rand_pos_int or run_all_tests:
    # Make sure that get_rand_pos_int returns an integer.
    run_func_tests(get_rand_pos_int, [
        IOPair((), (int,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_pos_int return type")
    # Make sure that get_rand_pos_int is positive.
    run_func_tests(get_rand_pos_int, [
        IOPair((), (0,)),
    ], assert_type=ASSERT_GREATER, test_desc="get_rand_pos_int return value")

if test_get_rand_neg_int or run_all_tests:
    # Make sure that get_rand_neg_int returns an integer.
    run_func_tests(get_rand_neg_int, [
        IOPair((), (int,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_neg_int return type")
    # Make sure that get_rand_neg_int is negative.
    run_func_tests(get_rand_neg_int, [
        IOPair((), (0,)),
    ], assert_type=ASSERT_LESS, test_desc="get_rand_neg_int return value")

if test_get_rand_int_list or run_all_tests:
    # Make sure that all elements in the get_rand_int_list output are integers.
    run_func_tests(get_rand_int_list, [
        IOPair((1,), (int,)),
        IOPair((10,), (int,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_int_list return type")
    # Make sure that get_rand_int_list returns lists of the correct lengths.
    run_func_tests(get_rand_int_list, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_int_list return length")
    # Make sure that get_rand_int_list raises errors for incorrect parameters.
    run_func_tests(get_rand_int_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_int_list errors for incorrect parameters")

if test_get_rand_pos_int_list or run_all_tests:
    # Make sure that all elements in the get_rand_pos_int_list output are integers.
    run_func_tests(get_rand_pos_int_list, [
        IOPair((1,), (int,)),
        IOPair((10,), (int,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_pos_int_list return type")
    # Make sure that all elements in get_rand_pos_int_list are greater than zero.
    run_func_tests(get_rand_pos_int_list, [
        IOPair((1,), (0,)),
        IOPair((10,), (0,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_GREATER, test_desc="get_rand_pos_int_list return values")
    # Make sure that get_rand_pos_int_list returns lists of the correct lengths.
    run_func_tests(get_rand_pos_int_list, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_pos_int_list return length")
    # Make sure that get_rand_pos_int_list raises errors for incorrect parameters.
    run_func_tests(get_rand_pos_int_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_pos_int_list errors for incorrect parameters")

if test_get_rand_neg_int_list or run_all_tests:
    # Make sure that all elements in the get_rand_neg_int_list output are integers.
    run_func_tests(get_rand_neg_int_list, [
        IOPair((1,), (int,)),
        IOPair((10,), (int,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_neg_int_list return type")
    # Make sure that all elements in get_rand_neg_int_list are less than zero.
    run_func_tests(get_rand_neg_int_list, [
        IOPair((1,), (0,)),
        IOPair((10,), (0,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_LESS, test_desc="get_rand_neg_int_list return values")
    # Make sure that get_rand_neg_int_list returns lists of the correct lengths.
    run_func_tests(get_rand_neg_int_list, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_neg_int_list return length")
    # Make sure that get_rand_neg_int_list raises errors for incorrect parameters.
    run_func_tests(get_rand_neg_int_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_neg_int_list errors for incorrect parameters")

if test_get_rand_float or run_all_tests:
    # Make sure that get_rand_float returns a float.
    run_func_tests(get_rand_float, [
        IOPair((), (float,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_float return type")

if test_get_rand_pos_float or run_all_tests:
    # Make sure that get_rand_pos_float returns a float.
    run_func_tests(get_rand_pos_float, [
        IOPair((), (float,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_pos_float return type")
    # Make sure that get_rand_pos_float is positive.
    run_func_tests(get_rand_pos_int, [
        IOPair((), (0.0,)),
    ], assert_type=ASSERT_GREATER, test_desc="get_rand_pos_float return value")

if test_get_rand_neg_float or run_all_tests:
    # Make sure that get_rand_neg_float returns a float.
    run_func_tests(get_rand_neg_float, [
        IOPair((), (float,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_neg_float return type")
    # Make sure that get_rand_neg_float is negative.
    run_func_tests(get_rand_neg_int, [
        IOPair((), (0.0,)),
    ], assert_type=ASSERT_LESS, test_desc="get_rand_neg_float return value")

if test_get_rand_float_list or run_all_tests:
    # Make sure that all elements in the get_rand_float_list output are floats.
    run_func_tests(get_rand_float_list, [
        IOPair((1,), (float,)),
        IOPair((10,), (float,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_float_list return type")
    # Make sure that get_rand_float_list returns lists of the correct lengths.
    run_func_tests(get_rand_float_list, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_float_list return length")
    # Make sure that get_rand_float_list raises errors for incorrect parameters.
    run_func_tests(get_rand_float_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_float_list errors for incorrect parameters")

if test_get_rand_pos_float_list or run_all_tests:
    # Make sure that all elements in the get_rand_pos_float_list output are floats.
    run_func_tests(get_rand_pos_float_list, [
        IOPair((1,), (float,)),
        IOPair((10,), (float,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_pos_float_list return type")
    # Make sure that all elements in get_rand_pos_float_list are greater than zero.
    run_func_tests(get_rand_pos_float_list, [
        IOPair((1,), (0.0,)),
        IOPair((10,), (0.0,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_GREATER, test_desc="get_rand_pos_float_list return values")
    # Make sure that get_rand_pos_float_list returns lists of the correct lengths.
    run_func_tests(get_rand_pos_float_list, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_pos_float_list return length")
    # Make sure that get_rand_pos_float_list raises errors for incorrect parameters.
    run_func_tests(get_rand_pos_float_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_pos_float_list errors for incorrect parameters")

if test_get_rand_neg_float_list or run_all_tests:
    # Make sure that all elements in the get_rand_neg_float_list output are floats.
    run_func_tests(get_rand_neg_float_list, [
        IOPair((1,), (float,)),
        IOPair((10,), (float,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_neg_float_list return type")
    # Make sure that all elements in get_rand_neg_float_list are less than zero.
    run_func_tests(get_rand_neg_float_list, [
        IOPair((1,), (0.0,)),
        IOPair((10,), (0.0,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_LESS, test_desc="get_rand_neg_float_list return values")
    # Make sure that get_rand_neg_float_list returns lists of the correct lengths.
    run_func_tests(get_rand_neg_float_list, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_neg_float_list return length")
    # Make sure that get_rand_neg_float_list raises errors for incorrect parameters.
    run_func_tests(get_rand_neg_float_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_neg_float_list errors for incorrect parameters")

if test_get_rand_letter_lowercase or run_all_tests:
    # Make sure that get_rand_letter_lowercase returns a string.
    run_func_tests(get_rand_letter_lowercase, [
        IOPair((),(str,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_letter_lowercase return type")
    # Make sure that get_rand_letter_lowercase returns a lowercase a-z letter.
    run_func_tests(get_rand_letter_lowercase, [
        IOPair((), ("abcdefghijklmnopqrstuvwxyz",)),
    ], assert_type=ASSERT_IN_SET, test_desc="get_rand_letter_lowercase return type")
    # Make sure that get_rand_letter_lowercase returns a string of length one.
    run_func_tests(get_rand_letter_lowercase, [
        IOPair((), (1,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_letter_lowercase return length")

if test_get_rand_letter_uppercase or run_all_tests:
    # Make sure that get_rand_letter_uppercase returns a string.
    run_func_tests(get_rand_letter_uppercase, [
        IOPair((),(str,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_letter_uppercase return type")
    # Make sure that get_rand_letter_uppercase returns a uppercase A-Z letter.
    run_func_tests(get_rand_letter_uppercase, [
        IOPair((), ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
    ], assert_type=ASSERT_IN_SET, test_desc="get_rand_letter_uppercase return type")
    # Make sure that get_rand_letter_uppercase returns a string of length one.
    run_func_tests(get_rand_letter_uppercase, [
        IOPair((), (1,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_letter_uppercase return length")

if test_get_rand_letter_mixedcase or run_all_tests:
    # Make sure that get_rand_letter_mixedcase returns a string.
    run_func_tests(get_rand_letter_mixedcase, [
        IOPair((),(str,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_letter_mixedcase return type")
    # Make sure that get_rand_letter_mixedcase returns a mixedcase A-Z letter.
    run_func_tests(get_rand_letter_mixedcase, [
        IOPair((), ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
    ], assert_type=ASSERT_IN_SET, test_desc="get_rand_letter_mixedcase return type")
    # Make sure that get_rand_letter_mixedcase returns a string of length one.
    run_func_tests(get_rand_letter_mixedcase, [
        IOPair((), (1,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_letter_mixedcase return length")

if test_get_rand_letter_list or run_all_tests:
    # Make sure that all elements in the get_rand_letter_list output are strings.
    run_func_tests(get_rand_letter_list, [
        IOPair((1,), (str,)),
        IOPair((10,), (str,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_letter_list return type")
    # Make sure that get_rand_letter_list returns lists of the correct lengths.
    run_func_tests(get_rand_letter_list, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_letter_list return length")
    # Make sure that get_rand_letter_list returns a list that only contains a-z or A-Z letters.
    run_func_tests(get_rand_letter_list, [
        IOPair((25,), ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
    ], assert_type=ASSERT_LIST_ELEMENTS_IN_SET, test_desc="get_rand_letter_list return values")
    # Make sure that get_rand_letter_list raises errors for incorrect parameters.
    run_func_tests(get_rand_letter_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_letter_list errors for incorrect parameters")

if test_get_rand_uppercase_letter_list or run_all_tests:
    # Make sure that all elements in the get_rand_uppercase_letter_list output are strings.
    run_func_tests(get_rand_uppercase_letter_list, [
        IOPair((1,), (str,)),
        IOPair((10,), (str,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_uppercase_letter_list return type")
    # Make sure that get_rand_uppercase_letter_list returns lists of the correct lengths.
    run_func_tests(get_rand_uppercase_letter_list, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_uppercase_letter_list return length")
    # Make sure that get_rand_uppercase_letter_list returns a list that only contains a-z or A-Z letters.
    run_func_tests(get_rand_uppercase_letter_list, [
        IOPair((25,), ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
    ], assert_type=ASSERT_LIST_ELEMENTS_IN_SET, test_desc="get_rand_uppercase_letter_list return values")
    # Make sure that get_rand_uppercase_letter_list raises errors for incorrect parameters.
    run_func_tests(get_rand_uppercase_letter_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_uppercase_letter_list errors for incorrect parameters")

if test_get_rand_lowercase_letter_list or run_all_tests:
    # Make sure that all elements in the get_rand_lowercase_letter_list output are strings.
    run_func_tests(get_rand_lowercase_letter_list, [
        IOPair((1,), (str,)),
        IOPair((10,), (str,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_lowercase_letter_list return type")
    # Make sure that get_rand_lowercase_letter_list returns lists of the correct lengths.
    run_func_tests(get_rand_lowercase_letter_list, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_lowercase_letter_list return length")
    # Make sure that get_rand_lowercase_letter_list returns a list that only contains a-z or A-Z letters.
    run_func_tests(get_rand_lowercase_letter_list, [
        IOPair((25,), ("abcdefghijklmnopqrstuvwxyz",)),
    ], assert_type=ASSERT_LIST_ELEMENTS_IN_SET, test_desc="get_rand_lowercase_letter_list return values")
    # Make sure that get_rand_lowercase_letter_list raises errors for incorrect parameters.
    run_func_tests(get_rand_lowercase_letter_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_lowercase_letter_list errors for incorrect parameters")

if test_get_rand_az_string_lowercase or run_all_tests:
    # Make sure that get_rand_az_string_lowercase returns a string.
    run_func_tests(get_rand_az_string_lowercase, [
        IOPair((1,),(str,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_az_string_lowercase return type")
    # Make sure that get_rand_az_string_lowercase returns a lowercase a-z letter.
    run_func_tests(get_rand_az_string_lowercase, [
        IOPair((1,), ("abcdefghijklmnopqrstuvwxyz",)),
        IOPair((10,), ("abcdefghijklmnopqrstuvwxyz",)),
        IOPair((25,), ("abcdefghijklmnopqrstuvwxyz",)),
    ], assert_type=ASSERT_CHARS_IN_SET, test_desc="get_rand_az_string_lowercase return type")
    # Make sure that get_rand_letter_lowercase returns a string of length one.
    run_func_tests(get_rand_az_string_lowercase, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_az_string_lowercase return length")

if test_get_rand_az_string_uppercase or run_all_tests:
    # Make sure that get_rand_az_string_uppercase returns a string.
    run_func_tests(get_rand_az_string_uppercase, [
        IOPair((1,),(str,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_az_string_uppercase return type")
    # Make sure that get_rand_az_string_uppercase returns a uppercase a-z letter.
    run_func_tests(get_rand_az_string_uppercase, [
        IOPair((1,), ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
        IOPair((10,), ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
        IOPair((25,), ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
    ], assert_type=ASSERT_CHARS_IN_SET, test_desc="get_rand_az_string_uppercase return type")
    # Make sure that get_rand_letter_uppercase returns a string of length one.
    run_func_tests(get_rand_az_string_uppercase, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_az_string_uppercase return length")

if test_get_rand_az_string_mixedcase or run_all_tests:
    # Make sure that get_rand_az_string_mixedcase returns a string.
    run_func_tests(get_rand_az_string_mixedcase, [
        IOPair((1,),(str,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_az_string_mixedcase return type")
    # Make sure that get_rand_az_string_mixedcase returns a mixedcase a-z letter.
    run_func_tests(get_rand_az_string_mixedcase, [
        IOPair((1,), ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
        IOPair((10,), ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
        IOPair((25,), ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",)),
    ], assert_type=ASSERT_CHARS_IN_SET, test_desc="get_rand_az_string_mixedcase return type")
    # Make sure that get_rand_letter_mixedcase returns a string of length one.
    run_func_tests(get_rand_az_string_uppercase, [
        IOPair((1,), (1,)),
        IOPair((10,), (10,)),
        IOPair((25,), (25,)),
    ], assert_type=ASSERT_LENGTH, test_desc="get_rand_az_string_mixedcase return length")