from test_helper_by_delica import *


def always_true():
    """Function that always returns True"""
    return True

test_bool_func(always_true, true_inputs=[()], test_desc="always true function")

def always_false():
    """Function that always returns False"""
    return False

test_bool_func( always_false, false_inputs=[()], test_desc="always false function")



def is_int(val):
    return isinstance(val, int)

test_bool_func(is_int, true_inputs=[(1,),(2,),(-10,)], false_inputs=[(1.0,),(2.0,),("",),('a',),("abc",)], test_desc="is_int function")

def can_convert_to_int(val):
    can_convert = isinstance(val, int)
    if not can_convert:
        try:
            int_val = int(val)
            can_convert = True
        except ValueError:
            can_convert = False
        except TypeError:
            can_convert = False
    return can_convert

test_bool_func(can_convert_to_int, true_inputs=[(1,),(2.0,),("-10",)], false_inputs=[("hello",),("1ab",),([],)],
               test_desc="can_convert_to_int function"),

def list_has_val(search_list, val_to_find):
    return val_to_find in search_list

test_bool_func(list_has_val, true_inputs=[([1],1),([1,2],2),(["a","ab","abc"],"a")],
               false_inputs=[([],0),([1],2),([1,2,3],4),(["a",1,"b"],2)])