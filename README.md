# test-helper-by-delica
## Purpose
This Python package simplifies the creation and execution of unittest test cases,  
in order to help programmers efficiently develop and run tests for their Python software.
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
We then use the test helper package to create a unittest TestCase object.
````
import test_helper_by_delica as test_lib 
test_obj = test_lib.create_unittest_obj()
````
Now we can call the boolean testing function to check whether always_true returns the expected result.
````
test_lib.test_bool_func(test_obj, always_true, true_inputs=())
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
    
test_lib.test_bool_func(test_obj, always_false, false_inputs=())
````
We then have the following output:
````
TESTING ALWAYS FALSE FUNCTION
Test #1 of 1
Testing always_false function for input ()
SUCCESS: input=() -> output=False
ALL 1 TESTS COMPLETED FOR ALWAYS FALSE FUNCTION
````
The Usage section below provides additional examples of how you can test your own functions with the test helper package.
## Usage

## Citation