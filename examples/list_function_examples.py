"""
Script demonstrating how we can use the test helper package to evaluate functions that receive or generate Python lists.
The optional runtime arguments below allow the user to choose which list examples they would like to run. If no runtime
flags are used, this script will run all of the list examples.

Parameters
----------
---run_empty_list_demo : bool, default False
    Boolean flag for whether the empty list example should be run.
---run_single_element_list_demo : bool, default False
    Boolean flag for whether the single-element list  example should be run.
---run_multi_element_list_demo : bool, default False
    Boolean flag for whether the multiple-element list example should be run.
---run_nested_list_demo : bool, default False
    Boolean flag for whether the nested list function example should be run.
---run_search_list_demo : bool, default False
    Boolean flag for whether the search list example should be run.
---run_concat_list_demo : bool, default False
    Boolean flag for whether the concatenate list example should be run.

"""

# Import the test helper functions
from src import test_helper_funcs as test_lib

# Import the IOPair class
from src.IOPair import IOPair

# Import argparse to parse the runtime arguments that allow the user to select which examples they want to run.
import argparse

# Declare some default integer lists that we can use in our sample tests.
DEFAULT_INT_VAL = 0
"Default integer value that should be used when constructing input lists."
DEFAULT_ONE_ELEMENT_LIST = [DEFAULT_INT_VAL]
"Default list with only one element (contains the default integer value)."
DEFAULT_MULTI_ELEMENT_LIST = [DEFAULT_INT_VAL, DEFAULT_INT_VAL+1, DEFAULT_INT_VAL+2]
"Default list with more than one element (contains the default integer value and the two integers that come after it)."
DEFAULT_NESTED_LIST = [[DEFAULT_INT_VAL],
                       [DEFAULT_INT_VAL+1, DEFAULT_INT_VAL+2],
                       [DEFAULT_INT_VAL-1,DEFAULT_INT_VAL-2,DEFAULT_INT_VAL-3]]
"Default nested list (i.e., a list that contains lists as elements)."

# Parse the runtime argument flags to determine which list examples should be run
parser = argparse.ArgumentParser(description="Parser for function examples script")
"Parser for runtime arguments."
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
"Parsed runtime arguments."
run_empty_list_demo = args.run_empty_list_demo
"Runtime flag for whether we should run the empty list example."
run_one_element_list_demo = args.run_single_element_list_demo
"Runtime flag for whether we should run the single-element list example."
run_multi_element_list_demo = args.run_multi_element_list_demo
"Runtime flag for whether we should run multiple-element list example."
run_nested_list_demo = args.run_nested_list_demo
"Runtime flag for whether we should run the nested list example."
run_search_list_demo = args.run_search_list_demo
"Runtime flag for whether we should run the search list example."
run_concat_lists_demo = args.run_concat_lists_demo
"Runtime flag for whether we should run the concatenated list example."
any_demos = run_empty_list_demo or run_one_element_list_demo or run_multi_element_list_demo \
            or run_nested_list_demo or run_search_list_demo or run_concat_lists_demo
"Boolean for whether the user has selected any demos with the runtime flags."
run_all_demos = not any_demos
"Boolean for whether all demos should be run (default behaviour if no runtime flags are used)."
# If no demos are selected, we will run all of them.
run_empty_list_demo = run_empty_list_demo or run_all_demos
run_one_element_list_demo = run_one_element_list_demo or run_all_demos
run_multi_element_list_demo = run_multi_element_list_demo or run_all_demos
run_nested_list_demo = run_nested_list_demo or run_all_demos
run_search_list_demo = run_search_list_demo or run_all_demos
run_concat_lists_demo = run_concat_lists_demo or run_all_demos

# Define the list-based functions that we will use for the examples.
def return_empty_list():
    """Returns an empty list."""
    return []

def return_one_element_list():
    """Returns a list with one element."""
    return DEFAULT_ONE_ELEMENT_LIST

def return_multi_element_list():
    """Returns a list with multiple elements."""
    return DEFAULT_MULTI_ELEMENT_LIST

def return_nested_list():
    """Returns a nested list."""
    return DEFAULT_NESTED_LIST

def find_int_vals_in_list(list_to_search):
    """Returns a list with all the integer values in the list_to_search parameter."""
    int_vals = []
    for val in list_to_search:
        if type(val) == int:
            int_vals.append(val)
    return int_vals

def concat_lists(list1, list2):
    """Returns the result of concatenating two lists (list1 and list2)."""
    return list1 + list2



if run_empty_list_demo:
    test_lib.run_func_tests(return_empty_list, [IOPair((),([],)),IOPair(DEFAULT_INT_VAL,TypeError)],
                   test_desc="return empty list function")

if run_one_element_list_demo:
    test_lib.run_func_tests(return_one_element_list, [IOPair((),DEFAULT_ONE_ELEMENT_LIST),
                                             IOPair(DEFAULT_INT_VAL,TypeError)],
                   test_desc="return single-element list function")

if run_multi_element_list_demo:
    test_lib.run_func_tests(return_multi_element_list, [IOPair((),DEFAULT_MULTI_ELEMENT_LIST),
                                             IOPair(DEFAULT_INT_VAL,TypeError)],
                   test_desc="return multi-element list function")


if run_nested_list_demo:
    test_lib.run_func_tests(return_nested_list, [IOPair((), DEFAULT_NESTED_LIST),
                                             IOPair(DEFAULT_INT_VAL, TypeError)],
                   test_desc="return nested list function")

if run_search_list_demo:
    test_lib.run_func_tests(find_int_vals_in_list, [IOPair([], []),
                                           IOPair([DEFAULT_INT_VAL], [DEFAULT_INT_VAL]),
                                             IOPair([1,2,3], [1,2,3]),
                                           IOPair([1,"a",1.0,2],[1,2]),
                                           IOPair(["abc","1",1.0,-20.0,-10],[-10]),
                                           IOPair(["abc","12",-10.22,True,False,"",[],[1,2]],[])],
                   test_desc="find int values in list function")

if run_concat_lists_demo:
    test_lib.run_func_tests(concat_lists, [IOPair(([],[]), []),
                                        IOPair(([1],[2]), [1,2]),
                                  IOPair(([1,2,3],[4,5,6]),[1,2,3,4,5,6]),
                                  IOPair((["a"],["b"]),["a", "b"]),
                                  IOPair((["1","2",True],["6","99",-111,-22222,"abcde*"]),
                                         ["1","2",True,"6","99",-111,-22222,"abcde*"]),
                                  IOPair([1,2],TypeError)],
                   test_desc="return concat list function")