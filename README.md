# test-helper-by-delica
## Purpose
This package simplifies the creation, execution, and analysis of unit tests in Python,
in order to help programmers more efficiently develop and validate their software.
## Installation
This package is available through the Python Package Index (PyPI).      
One can easily download the package with the following pip install statement:   
`pip install test_helper_by_delica`   

If you are a contributor who needs to test changes from the development branch,    
you can install the test version of the library from TestPyPI with the following line:   
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
test_lib.test_bool_func(always_true, true_inputs=[()], test_desc="always true function")
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
    
test_lib.test_bool_func(test_obj, always_false, false_inputs=[()], test_desc="always false function")
````
We then have the following output:
````
TESTING ALWAYS FALSE FUNCTION
Test #1 of 1
Testing always_false function for input ()
SUCCESS: input=() -> output=False
ALL 1 TESTS COMPLETED FOR ALWAYS FALSE FUNCTION
````
To see what happens if a test fails, we can try using the always_true function in our always_false test.
````
test_lib.test_bool_func(test_obj, always_false, true_inputs=[()], test_desc="always true function")
````
This call prints the following stdout output to inform the user that the test has failed:
````
TESTING ALWAYS TRUE FUNCTION
Test #1 of 1
Testing always_false function for input ()
FAILURE: ALWAYS_FALSE FUNCTION FOR INPUT () FAILED WITH INPUT = () EXPECTED_OUTPUT = True, ACTUAL_OUTPUT = False
ALL 1 TESTS COMPLETED FOR ALWAYS TRUE FUNCTION
````
Now suppose we want to test a boolean function that takes an input parameter. For example, let's use the is_even   
function below, which returns True if the input parameter is an integer and False if it is not.
````
def is_int(val):
    return isinstance(val, int)
````
For this function, we need to specify values that should yield True and values that should yield False. The test helper
package expects the input parameters for each individual test (e.g, testing whether the number 2 yields True) to be 
provided in the form of a tuple. If the input for a function only includes one parameter, please add a comma 
(e.g., (1,) instead of (1)) to ensure that you pass a tuple when you call the boolean test helper function.
````
test_bool_func(test_obj, is_int, true_inputs=[(1,),(2,)], false_inputs=[(1.0,),(1.0)], test_desc="is_int function")
````
The Usage section below provides additional examples of how you can test your own functions with the test helper package.
## Usage

## Citation