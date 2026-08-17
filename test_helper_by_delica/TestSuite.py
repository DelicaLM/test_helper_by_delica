import inspect
import docstring_parser
from TestParameter import TestParameter

class TestSuite:
    def __init__(self, func_handle):
        self.test_func = func_handle
        self.test_params = []
        func_sig = inspect.signature(func_handle)
        par_sig_details = inspect.getfullargspec(func_handle)
        par_names = []
        for par in par_sig_details.args:
            par_names.append(par)
        for par_name in par_names:
            new_test_par = TestParameter(par_name)
            self.test_params.append(new_test_par)
        test = 0

    def set_par_details(self, par_name, par_type = None, default_val = None, min_val = None, max_val = None,
                        other_illegal_values = None):
        par_index = 0
        found_par = False
        while par_index < len(self.test_params) and not found_par:
            found_par = self.test_params[par_index].par_name == par_name
            if not found_par:
                par_index += 1
        if not found_par:
            raise ValueError(f"Parameter with name {par_name} not found in the Test Suite for the function "
                             + f"{self.test_func.__name__},")







def add_one(int_val):
    return int_val + 1

test_suite = TestSuite(add_one)