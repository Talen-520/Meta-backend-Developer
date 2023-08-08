import addition 
import pytest

def test_add():
    assert addition.add(2,3) == 5

def test_sub():
    assert addition.sub(4,5) == -1
    assert addition.sub(1,5) == -4
'''
def test_sub():
    pass
def test_sub():
    True
'''
#in terminal run python -m pytest Pytest\test_addtion.py
#run  test over a specific function: python -m pytest Pytest\test_addtion.py::test_add
#all the assert statements within a given function should return a true value for the test to pass

#Flags used
'''
For example, -v is the flag:

python3 -m pytest abc.py -v

'''
#Some other flag options are:

'''
-v for verbose
-q quiet mode
-s allows the print statement inside the functions to be executed
-x is to flag the tests to stop execution after first failure
-m is used to mark a specific function
-k is a flag for searching and running tests with a specific keyword
--tb is to disable the traceback code of errors
--maxfail n specifies maximum number of test fails allowed
'''


'''
Fixtures
Fixtures are a type of function that is applied to functions to be tested. 
These functions must run before that test is executed. The purpose of fixtures is to 
supply data from multiple sources including URLs and databases to the test
before running the test. Fixtures are used in cases where code repeats initialization.

Format:

@pytest.fixture 

Markers
Markers are used to 'mark' specific functions to be executed by letting users create special names. 
There are many built-in markers such as xfail, xpass, skip and so on.

They follow a format such as:

@pytest.mark.<markername> 

For example:

@pytest.mark.alpha 

Running the specific marked test in the command line can be done with the following command:

pytest -m <markername> -v 

Which will be as follows for a marker called alpha.

pytest -m alpha -v 
'''