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
    run_func_tests(get_rand_bool, [
        IOPair((),(bool,))
    ], assert_type=ASSERT_TYPE)
    run_func_tests(get_rand_bool, [
        IOPair((), (bool,))
    ], assert_type=ASSERT_TYPE)
    run_func_tests(get_rand_bool, [
        IOPair((), ([True, False],))
    ], assert_type=ASSERT_IN_SET)

if test_get_rand_bool_list or run_all_tests:
    run_func_tests(get_rand_bool_list, [
        IOPair((), (list[bool],))
    ])