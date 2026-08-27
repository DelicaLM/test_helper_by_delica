import inspect
import docstring_parser
from TestParameter import TestParameter
import test_helper_funcs as test_lib

class TestSuite:
    def __init__(self, func_handle):
        self.test_func = func_handle
        self.test_params = []
        self.return_type = None
        self.return_types = []
        func_sig = inspect.signature(func_handle)
        if func_sig.return_annotation != inspect.Parameter.empty and isinstance(func_sig.return_annotation, type):
            self.return_type = func_sig.return_annotation
            self.return_types.append(self.return_type)
        for name, param in func_sig.parameters.items():
            par_name = name
            par_type = None
            par_default = None
            if param.annotation != inspect.Parameter.empty and isinstance(param.annotation, type):
                par_type = param.annotation
            if param.default != inspect.Parameter.empty:
                par_default = param.default
            new_param = TestParameter(par_name, par_type, par_default)
            self.test_params.append(new_param)
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

    def run_type_tests(self):
        io_pairs = []
        test_lib.run_func_tests(self.test_func, io_pairs)








def add_one(int_val : int = 1) -> int:
    return int_val + 1

test_suite = TestSuite(add_one)