# test-helper-by-delica README
## Purpose
This package simplifies the creation, execution, and analysis of unit tests in Python,
in order to help programmers more efficiently develop and validate their software.
## Installation
This package is available through the Python Package Index (PyPI).      
One can easily download the package with the following pip install statement:   
`pip install test_helper_by_delica`   

If you are a contributor who needs to test changes from the development branch,    
you can install the test version of the library from TestPyPI with the following command:   
`pip install --index-url https://test.pypi.org/simple/test_helper_by_delica`    

If you are not a contributor to this project, please only use the production version     
that is deployed on PyPI and can be downloaded with `pip install test_helper_by_delica`.    
The production version is the most stable release of the test helper package.    
## Getting Started
After installation, all we need to start using the package is a function that we want to test.   
For a simple example, we can define a boolean function that always returns True.  
````
def always_true():    
    return True   
````
Now we can call the boolean testing function from the package to check whether always_true returns the expected result.
````
import test_helper_by_delica 
test_helper_by_delica.test_bool_func(always_true, true_inputs=[()], test_desc="always true function")
````
This function call generates the following output:
````
TESTING ALWAYS TRUE FUNCTION
Test #1 of 1
Testing always_true function for input ()
SUCCESS: input=() -> output=True
ALL 1 TESTS COMPLETED FOR ALWAYS TRUE FUNCTION
````
Similarly, we can test a function that always returns False.
````
def always_false():    
    return False
    
test_helper_by_delica.test_bool_func(always_false, false_inputs=[()], test_desc="always false function")
````
We then have the following output:
````
TESTING ALWAYS FALSE FUNCTION
Test #1 of 1
Testing always_false function for input ()
SUCCESS: input=() -> output=False
ALL 1 TESTS COMPLETED FOR ALWAYS FALSE FUNCTION
````
To see what happens if a test fails, we can try using the always_false function in our always_true test.
````
test_helper_by_delica.test_bool_func(test_obj, always_false, true_inputs=[()], test_desc="always true function")
````
This call prints the following stdout output to inform the user that the test has failed:
````
TESTING ALWAYS TRUE FUNCTION
Test #1 of 1
Testing always_false function for input ()
FAILURE: ALWAYS_FALSE FUNCTION FOR INPUT () FAILED WITH INPUT = () EXPECTED_OUTPUT = True, ACTUAL_OUTPUT = False
ALL 1 TESTS COMPLETED FOR ALWAYS TRUE FUNCTION
````
Now suppose we want to test a boolean function that takes an input parameter. For example, let's use the is_int   
function below, which returns True if the input parameter is an integer and False if it is not.
````
def is_int(val):
    return isinstance(val, int)
````
For this function, we need to specify values that should yield True and values that should yield False. The test helper
package expects the input parameters for each individual test (e.g, testing whether the number 2 yields True) to be 
provided in the form of a tuple. If your input or output tuple has only one element, you can pass the object on its 
own without adding parentheses (e.g., can pass 1 instead of (1,) for an input tuple), because the test helper package 
will take care of converting your single input or return parameter to a tuple format. 
````
test_helper_by_delica.test_bool_func(is_int, true_inputs=[1,2], false_inputs=[1.0,"2"], test_desc="is_int function")
````
If we have a function with two parameters, such as the sum function below, we need to pass the inputs as tuples (e.g.,
(1, 2), (0, 0), (3, 2), etc.). If we do not include the parentheses, the test helper function cannot accurately determine
the number of input parameters that the test function should receive. 
````
def calc_sum(int1, int2):
    return int1 + int2
test_helper_by_delica.run_func_tests(calc_sum, [IOPair((1, 2), 3), IOPair((0, 0), 0), IOPair((3, 2), 5)], 
test_desc="sum calculator function")
````
In the above example, we use run_func_tests from the test helper package instead of test_bool_func because the sum
function does not return a boolean value. The more general run_func_tests function can test whether any type of return
value is correct based on user-provided criteria. If a user wants to verify whether their test function raises an 
exception, they simply need to set the expected test output to the correct exception type (e.g., TypeError, ValueError,
etc.), as demonstrated below. 
````
def is_int_error_if_false(val):
    is_int_val = isinstance(val, int)
    if not is_int_val:
        raise TypeError("val is not an integer")
    return is_int_val
    
test_helper_by_delica.run_func_tests(is_int_error_if_false, [IOPair(1, True), IOPair(1.0, TypeError), IOPair((3, 2), 5)], 
               test_desc="is integer error if false function")
````
The main difference between run_func_tests and test_bool_func, besides the types of functions that they can validate, 
is that run_func_tests requires a list of IOPair objects to specify the 
expected input-output pairs for the tests. For example, if our input numbers are 1 and 2 and we expect the sum value to
be 3, we will pass this information to run_func_tests in the form IOPair((1, 2), 3). If we instead test a function that
returns two numbers which equal an input parameter when added together, we could have a test with IOPair(3, (1, 2)).
The test_bool_func function does not require IOPair objects to define expected outputs, because there are only two 
possible outcomes for boolean functions. The test helper package class includes the IOPair class to facilitate cases
in which we need to test a wide range of possible output types. 

The Usage section below provides additional examples of how you can test your own functions with the test helper 
package.
## Usage
This package supports three different methods for testing Python code. If you only need to run one test, use the 
run_single_test function, as demonstrated below with a test function that returns the sum of two numbers.
````
def calc_sum(int1, int2):
    return int1 + int2

test_helper_by_delica.run_single_test(calc_sum, test_input=(1, 2), expected_output=3, test_desc="Sum Test 1")
````
If you need to run multiple tests, use run_func_tests to check how your function responds to multiple input scenarios.
For each test case, provide an IOPair object that contains the input for the test and the expected output. The code
segment below provides an example of how to format these IOPair objects for our sum calculator function.
````
test_helper_by_delica.run_func_tests(calc_sum, [IOPair((1, 2), 3), IOPair((2, 2), 4)], test_desc="Sum Test Suite")
````
Although the above example only uses integers, the IOPair class accepts any data types for test inputs and outputs. The 
package currently does not support file-based output checking (e.g., checking if a function creates a file or that the
contents of an output file are correct). However, file IO will be included in a future version. 

If your function returns a boolean output (True or False), you can skip the creation of IOPair objects by using the
test_bool_func function in this package.
````
def is_pos(num):
    return num > 0
    
test_helper_by_delica.test_bool_func(is_pos, true_inputs=[1, 2, 0.1, 100], false_inputs=[-1, -0.1, -100, -1203], 
test_desc="Bool Function Tests")
````
Each of the three aforementioned functions (run_single_test, run_func_tests, and test_bool_func) can also verify that
your functions throw errors in the correct circumstances. For example, suppose that we want our boolean function to
throw a ValueError if the input is zero or negative.
````
def is_pos_with_error(num)
    result = num > 0
    if not result:
        raise ValueError()
    return result

test_helper_by_delica.test_bool_func(is_pos, true_inputs=[1, 2, 0.1, 100], false_inputs=[-1, -0.1, -100, -1203], 
test_desc="Bool Function Tests With Value Error", error_if_false=True, error_type=ValueError)
````
For additional information on how this package can accommodate your testing needs, please see the full documentation at
[https://delicalm.github.io/test_helper_by_delica/](https://delicalm.github.io/test_helper_by_delica/).
## Citation
To reference this Python package, please use the following citation.
### APA Format
Leboe-McGowan, D. S. (2026). Test helper by delica (Version 1.0.X) [Source code]. GitHub. 
[https://github.com/DelicaLM/test_helper_by_delica](https://github.com/DelicaLM/test_helper_by_delica)