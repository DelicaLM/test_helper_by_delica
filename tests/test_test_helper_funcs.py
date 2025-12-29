import test_helper_by_delica.test_helper_funcs as test_lib

def no_param_no_return():
    return

def one_param_no_return(param):
    return

def two_param_no_return(param1, param2):
    return


test_run_single_test = True
test_run_func_tests = False

test_with_no_param_no_return = False
test_with_one_param_no_return = False
test_with_two_param_no_return = True

if test_run_single_test:
    print("TESTING RUN_SINGLE_TEST FUNCTION")
    if test_with_no_param_no_return:
        #Test whether the run-single-test function correctly handles a test function with no parameters and no return values.
        #Success Case: The run-single-test function should conclude that the no-param-no-return function
        #              is working properly when it returns nothing.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_no_return,(),(),test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(True,),
                                 test_desc="run-single-test function on test function with no parameters and no return value (success case)")
        print("")
        #Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output from
        #           no-param-no-return does not match the actual output.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(no_param_no_return,(),(True,),test_lib.ASSERT_EQUAL,
                                             "function with no parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with no parameters and no return value "
                                           + "(fail case)")
        print("")
    if test_with_one_param_no_return:
        #Test whether the run-single-test function correctly handles a test function with one parameter and no return value.
        #Success Case: The run-single-test function should conclude that the one-param-no-return function
        #              is working properly when it returns nothing.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(one_param_no_return,(0,),(),test_lib.ASSERT_EQUAL,
                                             "function with one parameter and no return value"),
                                 expected_output=(True,),
                                 test_desc="run-single-test function on test function with one parameter and no return value "
                                           + "(success case)")
        print("")
        #Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output from
        #           one-param-no-return does not match the actual output.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(one_param_no_return,(0,),(True,),test_lib.ASSERT_EQUAL,
                                             "function with one parameter and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with one parameter and no return value "
                                          + "(fail case)")
        print("")
        #Fail Case: Make sure that the run-single-test function raises an Assertion error if the one-param-no-return
        #           function raises an unexpected error (which we trigger by not passing the required parameter).
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(one_param_no_return,(),(True,),test_lib.ASSERT_EQUAL,
                                             "function with one parameter and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with one parameter and no return value "
                                          + "(fail case)")
        print("")
    if test_with_two_param_no_return:
        #Test whether the run-single-test function correctly handles a test function with two parameters and no return value.
        #Success Case: The run-single-test function should conclude that the two-param-no-return function
        #              is working properly when it returns nothing.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(two_param_no_return,(0,0),(),test_lib.ASSERT_EQUAL,
                                             "function with two parameters and no return value"),
                                 expected_output=(True,),
                                 test_desc="run-single-test function on test function with two parameters and no return value "
                                           + "(success case)")
        print("")
        # Fail Case: Make sure that the run-single-test function raises an Assertion error if the expected output from
        #           two-param-no-return does not match the actual output.
        test_lib.run_single_test(test_lib.run_single_test,
                                 test_input=(two_param_no_return,(0,0),(True,),test_lib.ASSERT_EQUAL,
                                             "function with two parameters and no return value"),
                                 expected_output=(AssertionError,),
                                 test_desc="run-single-test function on test function with two parameters and no return value "
                                          + "(fail case)")
        print("")

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
