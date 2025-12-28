from test_helper_by_delica import *

test_obj = create_unittest_obj()

def always_true():
    """Function that always returns True"""
    return True

#test_bool_func(test_obj, always_true, true_inputs=[()], test_desc="always true function")

run_func_tests(test_obj, always_true)
def always_false():
    """Function that always returns False"""
    return False

#test_bool_func(test_obj, always_false, false_inputs=[()], test_desc="always false function")

#test_bool_func(test_obj, can_convert_to_int, true_inputs=[("1",)], test_desc="is_int function")

def is_int(val):
    return isinstance(val, int)

#test_bool_func(test_obj, is_int, true_inputs=[(1,),(2,),(-10,)], false_inputs=[(1.0,),(2.0,),("",),('a',),("abc",)], test_desc="is_int function")

def can_convert_to_int(val):
    can_convert = isinstance(val, int)
    if not can_convert:
        try:
            int_val = int(val)
        except ValueError:
            can_convert = False
    return can_convert


