from unittest import TestCase
import test_helper_by_delica.test_helper_funcs as test_lib

def test_func_always_true(test_int1=0, test_int2=0):
    return True

def test_func_always_false(test_int1=0, test_int2=0):
    return False

def test_func_is_int(test_input):
    return type(test_input) is int

class Test(TestCase):
    def test_test_bool_func(self):
        test_lib.test_bool_func(self, test_func_always_true, true_inputs=[(),(1,),(1,2)],
                                test_desc="always true function")
        test_lib.test_bool_func(self, test_func_always_false, false_inputs=[(),(1,),(1,2)],
                                test_desc="always false function")
        test = 0
