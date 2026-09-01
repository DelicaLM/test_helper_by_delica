import inspect
import docstring_parser
import random
from TestParameter import TestParameter
import test_helper_funcs as test_lib
from test_helper_by_delica import IOPair

DEFAULT_INT = 0
DEFAULT_FLOAT = 0.0
DEFAULT_STRING = ""
DEFAULT_BOOL = False

PAR_TYPES = [int, float, str]

def get_default_for_type(var_type : type = int):
    assert var_type in PAR_TYPES
    result = None
    if var_type is int:
        result = DEFAULT_INT
    elif var_type is float:
        result = DEFAULT_FLOAT
    elif var_type is str:
        result = DEFAULT_STRING
    elif var_type is bool:
        result = DEFAULT_BOOL
    return result

def get_rand_int(min_val : int = 0, max_val : int = 100) -> int:
    return random.randint(min_val, max_val)


def get_rand_float(min_val : float = 0.0, max_val : float = 1.0) -> float:
    return random.uniform(min_val, max_val)

# def get_rand_string(str_len = 1):
#


def get_rand_for_type(var_type : type = int):
    assert var_type in PAR_TYPES
    result = 0
    if var_type is int:
        result = DEFAULT_INT
    elif var_type is float:
        result = DEFAULT_FLOAT
    elif var_type is str:
        result = DEFAULT_STRING
    elif var_type is bool:
        result = DEFAULT_BOOL
    return result

def get_revised_tuple(tuple_to_revise, index_to_change, new_element):
    result = ()
    num_elements = len(tuple_to_revise)
    if index_to_change == 0:
        if num_elements == 1:
            result = (new_element,)
        else:
            result = (new_element,) + tuple_to_revise[1:]
    elif index_to_change < num_elements - 1:
        result = tuple_to_revise[:index_to_change] + (new_element,) \
                      + tuple_to_revise[index_to_change + 1:]
    else:
        result = tuple_to_revise[:index_to_change] + (new_element,)
    return result

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
            if par_default is None and par_type is not None:
                if par_type is int:
                    par_default = DEFAULT_INT
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

    def run_type_tests(self, expect_type_errors=True, num_rand_cases=1):
        io_pairs = []
        default_input_tuple = ()
        for param in self.test_params:
            default_input_tuple = default_input_tuple + (param.default_val,)
        # Test if the default tuple yields the expected return type.
        default_io_pair = IOPair(default_input_tuple, int)
        if expect_type_errors:
            param_index = 0
            while param_index < len(self.test_params):
                curr_param = self.test_params[param_index]
                curr_type = curr_param.par_type
                wrong_types = [par_type for par_type in PAR_TYPES if par_type != curr_type]
                for wrong_type in wrong_types:
                    wrong_default_val = get_default_for_type(wrong_type)
                    wrong_default_tuple = get_revised_tuple(default_input_tuple, param_index, wrong_default_val)
                    io_pairs.append(IOPair(wrong_default_tuple, TypeError))
                    # for i in range(num_rand_cases):
                    #     wrong_rand_val =
                param_index += 1
        io_pairs.append(default_io_pair)

        test_lib.run_func_tests(self.test_func, io_pairs, assert_type=test_lib.ASSERT_TYPE,
                                test_desc=f"{self.test_func.__name__} Function Parameter & Return Types")








def add_one(int_val : int = 1, float_val : float = 1.0, bool_val : bool = False) -> int:
    if type(int_val) != int:
        raise TypeError()
    if type(float_val) != float:
        raise TypeError()
    if type(bool_val) != bool:
        raise TypeError()
    return int_val + 1

test_suite = TestSuite(add_one)
test_suite.run_type_tests()