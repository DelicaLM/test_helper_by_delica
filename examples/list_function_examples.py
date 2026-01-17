"""
Script demonstrating how we can use the test helper package to evaluate functions that receive or output list objects.

The functions below are defined to help show the variety of list-based functions that we can efficiently test with
the helper package.

Functions
---------
return_empty_list()
    Returns empty list ([]).
return_one_element_list()
    Returns a list with only one element (value of the element depends on the DEFAULT_ONE_ELEMENT_LIST constant).
return_multi_element_list()
    Returns a list with more than one element (values in the list depend on the DEFAULT_MULTI_ELEMENT_LIST constant).
return_nested_list()
    Returns a list that itself contains lists as elements (values in the nested lists depend on the DEFAULT_NESTED_LIST
    constant).
find_int_vals_in_list(list_to_search)
    Returns a list with all the integer values in a list (returns empty list if there are no integer elements).
concat_lists(list1, list2)
    Returns the result of concatenating two lists.

Constants
---------
DEFAULT_INT_VALUE : int
    The default integer value that should be used when constructing input lists.



"""
import argparse

from test_helper_by_delica import *
import sys

DEFAULT_INT_VAL = 0
DEFAULT_ONE_ELEMENT_LIST = [DEFAULT_INT_VAL]
DEFAULT_MULTI_ELEMENT_LIST = [DEFAULT_INT_VAL, DEFAULT_INT_VAL+1, DEFAULT_INT_VAL+2]
DEFAULT_NESTED_LIST = [[DEFAULT_INT_VAL],
                       [DEFAULT_INT_VAL+1, DEFAULT_INT_VAL+2],
                       [DEFAULT_INT_VAL-1,DEFAULT_INT_VAL-2,DEFAULT_INT_VAL-3]]

run_all_demos = True
run_return_empty_list_demo = True
run_return_one_element_list_demo = True
run_return_multi_element_list_demo = True
run_return_nested_list_demo = True
run_find_int_vals_in_list_demo = True
run_concat_lists_demo = True

if __name__ == "main":
    parser = argparse.ArgumentParser(description="Parser for function examples script")
    parser.add_argument("--run_empty_list_demo", action="store_true",
        help="Boolean flag for whether the tests that use empty lists should be executed (optional argument).")
    parser.add_argument("--run_single_element_list_demo", action="store_true",
        help="Boolean flag for whether the tests that use lists of length one should be executed (optional argument).")
    parser.add_argument("--run_multi_element_list_demo", action="store_true",
    help="Boolean flag for whether the tests that use lists with multiple elements should be executed (optional "
         + "argument).")
    parser.add_argument("--run_nested_list_demo", action="store_true",
        help="Boolean flag for whether the tests that use nested lists should be executed (optional argument).")
    parser.add_argument("--run_search_list_demo", action="store_true",
        help="Boolean flag for whether the tests that search for an item in an input list should be executed "
             + "(optional argument).")
    parser.add_argument("--run_concat_lists_demo", action="store_true",
        help="Boolean flag for whether the tests concat two lists should be executed (optional argument).")
    args = parser.parse_args()
    run_return_empty_list_demo = args.run_empty_list_demo
    run_return_single_element_list_demo = args.run_single_element_list_demo
    run_return_multi_element_list_demo = args.run_multi_element_list_demo
    run_return_nested_list_demo = args.run_nested_list_demo
    run_search_list_demo = args.run_search_list_demo
    run_concat_lists_demo = args.run_concat_lists_demo
    any_demos = run_return_empty_list_demo or run_return_one_element_list_demo or run_return_multi_element_list_demo \
                or run_return_nested_list_demo or run_find_int_vals_in_list_demo or run_concat_lists_demo
    run_all_demos = not any_demos








def return_empty_list():
    return []

def return_one_element_list():
    return DEFAULT_ONE_ELEMENT_LIST

def return_multi_element_list():
    return DEFAULT_MULTI_ELEMENT_LIST

def return_nested_list():
    return DEFAULT_NESTED_LIST

def find_int_vals_in_list(list_to_search):
    int_vals = []
    for val in list_to_search:
        if type(val) == int:
            int_vals.append(val)
    return int_vals

def concat_lists(list1, list2):
    return list1 + list2



if run_all_demos or run_return_empty_list_demo:
    run_func_tests(return_empty_list, [IOPair((),([],)),IOPair(DEFAULT_INT_VAL,TypeError)],
                   test_desc="return empty list function")

if run_all_demos or run_return_one_element_list_demo:
    run_func_tests(return_one_element_list, [IOPair((),DEFAULT_ONE_ELEMENT_LIST),
                                             IOPair(DEFAULT_INT_VAL,TypeError)],
                   test_desc="return single-element list function")

if run_all_demos or run_return_multi_element_list_demo:
    run_func_tests(return_multi_element_list, [IOPair((),DEFAULT_MULTI_ELEMENT_LIST),
                                             IOPair(DEFAULT_INT_VAL,TypeError)],
                   test_desc="return multi-element list function")


if run_all_demos or run_return_nested_list_demo:
    run_func_tests(return_nested_list, [IOPair((), DEFAULT_NESTED_LIST),
                                             IOPair(DEFAULT_INT_VAL, TypeError)],
                   test_desc="return nested list function")

if run_all_demos or run_find_int_vals_in_list_demo:
    run_func_tests(find_int_vals_in_list, [IOPair([], []),
                                           IOPair([DEFAULT_INT_VAL], [DEFAULT_INT_VAL]),
                                             IOPair([1,2,3], [1,2,3]),
                                           IOPair([1,"a",1.0,2],[1,2]),
                                           IOPair(["abc","1",1.0,-20.0,-10],[-10]),
                                           IOPair(["abc","12",-10.22,True,False,"",[],[1,2]],[])],
                   test_desc="find int values in list function")

if run_all_demos or run_concat_lists_demo:
    run_func_tests(concat_lists, [IOPair(([],[]), []),
                                        IOPair(([1],[2]), [1,2]),
                                  IOPair(([1,2,3],[4,5,6]),[1,2,3,4,5,6]),
                                  IOPair((["a"],["b"]),["a", "b"]),
                                  IOPair((["1","2",True],["6","99",-111,-22222,"abcde*"]),
                                         ["1","2",True,"6","99",-111,-22222,"abcde*"]),
                                  IOPair([1,2],TypeError)],
                   test_desc="return concat list function")