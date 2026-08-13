import inspect
from TestParameter import TestParameter

class TestSuite:
    def __init__(self, func_handle):
        self.test_func = func_handle
        self.test_params = []
        func_sig = inspect.signature(func_handle)
        par_details = inspect.getfullargspec(func_handle)
        for par in par_details.args:
            new_test_par = TestParameter(par)
            self.test_params.append(par)
        test = 0






def add_one(int_val):
    return int_val + 1

test_suite = TestSuite(add_one)