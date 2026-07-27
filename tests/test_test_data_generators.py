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

test_get_rand_bool = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_bool function."
test_get_rand_bool_list = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_bool_list function."

test_get_rand_int = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_int function."
test_get_rand_pos_int = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_pos_int function."
test_get_rand_neg_int = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_neg_int function."
test_get_rand_int_list = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_int_list function."
test_get_rand_pos_int_list = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_pos_int_list function."

test_get_rand_float = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_float function."
test_get_rand_pos_float = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_pos_float function."
test_get_rand_neg_float = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_neg_float function."
test_get_rand_float_list = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_float_list function."

test_get_rand_letter_lowercase = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_letter_lowercase function."
test_get_rand_letter_uppercase = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_letter_uppercase function."
test_get_rand_letter_mixedcase = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_letter_mixedcase function."
test_get_rand_letter_list = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_letter_list function."

test_get_rand_az_string_lowercase = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_az_string_lowercase function."
test_get_rand_az_string_uppercase = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_az_string_uppercase function."
test_get_rand_az_string_mixedcase = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_az_string_mixedcase function."
test_get_rand_az_string_list = True
"bool : Boolean flag for whether or not to run the tests for the get_rand_az_string_list function."

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
    # Make sure that get_rand_int returns an integer.
    run_func_tests(get_rand_pos_int, [
        IOPair((), (int,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_pos_int return type")
    # Make sure that get_rand_int is positive.
    run_func_tests(get_rand_pos_int, [
        IOPair((), (0,)),
    ], assert_type=ASSERT_GREATER, test_desc="get_rand_pos_int return value")

if test_get_rand_neg_int or run_all_tests:
    # Make sure that get_rand_int returns an integer.
    run_func_tests(get_rand_neg_int, [
        IOPair((), (int,)),
    ], assert_type=ASSERT_TYPE, test_desc="get_rand_neg_int return type")
    # Make sure that get_rand_int is positive.
    run_func_tests(get_rand_neg_int, [
        IOPair((), (0,)),
    ], assert_type=ASSERT_LESS, test_desc="get_rand_neg_int return value")

if test_get_rand_int_list or run_all_tests:
    # Make sure that all elements in the get_rand_int_list output are booleans.
    run_func_tests(get_rand_int_list, [
        IOPair((1,), (int,)),
        IOPair((10,), (int,)),
    ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_int_list return type")
    # Make sure that get_rand_int_list raises errors for incorrect parameters.
    run_func_tests(get_rand_int_list, [
        IOPair(("",), (TypeError,)),
        IOPair((-1,), (ValueError,)),
    ], assert_type=ASSERT_EQUAL, test_desc="get_rand_int_list errors for incorrect parameters")

# if test_get_rand_pos_int_list or run_all_tests:
#     # Make sure that all elements in the get_rand_pos_int_list output are booleans.
#     run_func_tests(get_rand_pos_int_list, [
#         IOPair((1,), (int,)),
#         IOPair((10,), (int,)),
#     ], assert_type=ASSERT_LIST_ELEMENTS_TYPE, test_desc="get_rand_pos_int_list return type")
#     # Make sure that all elements in get_rand_pos_int_list are True or False
#     # (redundant with the previous test).
#     run_func_tests(get_rand_pos_int_list, [
#         IOPair((1,), ([True, False],)),
#         IOPair((10,), ([True, False],)),
#     ], assert_type=ASSERT_LIST_ELEMENTS_IN_SET, test_desc="get_rand_pos_int_list return values")
#     # Make sure that get_rand_pos_int_list raises errors for incorrect parameters.
#     run_func_tests(get_rand_pos_int_list, [
#         IOPair(("",), (TypeError,)),
#         IOPair((-1,), (ValueError,)),
#     ], assert_type=ASSERT_EQUAL, test_desc="get_rand_pos_int_list errors for incorrect parameters")