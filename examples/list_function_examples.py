"""
This script provides several examples of how one can use test_helper_by_delica to test list functions (i.e.,
functions that return a list object). We use the sample functions below to demonstrate how run_func_tests from the
test helper package allows us to quickly verify that Python code returns accurate list values for a wide range of
inputs.

Functions
---------
return_empty_list()
    Returns empty list ([]).
return_one_element_list()
    Returns a list with only one element (value of the element depends on the DEFAULT_ONE_ELEMENT_LIST constant).
return_multi_element_list()
    Returns a list with more than one element (values in the list depend on the DEFAULT_MULTI_ELEMENT_LIST constant).
return_nested_list()
    Returns a list that itself contains lists as elements (values depend on the DEFAULT_NESTED_ELEMENT_LIST constant).
find_int_vals_in_list(list_to_search)
    Returns a list with all the integer values in a list (returns empty list if there are no integer elements).


"""

