

class TestSuite:
    def __init__(self, func_handle):
        self.test_func = func_handle
        self.test_params = []

    def add_test_parameter(self, par_name, par_type, tuple_index=-1):
        self.test_params.append((par_name, par_type))