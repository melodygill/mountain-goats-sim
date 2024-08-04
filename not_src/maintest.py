# -*- coding: utf-8 -*-
"""
maintest.py - Figuring out how to use the unittest and logger built-in 
libraries by incorporating them into a prime number finding program.  Use the
insight that all prime numbers other than 2 and 3 are either 1 greater or 1
smaller than a multiple of six.  When testing numbers 0-100, this reduces the
numbers that must be tested by > 60%.
"""

import prime
import unittest

def is_prime_candidate(num_to_test):
    """
    Returns True if num_to_test is < 4 or a number 1 greater or 1 smaller
    than a multiple of six.  Otherwise returns False.

    """
    # Input checking
    if (num_to_test < 0):
        raise ValueError("is_prime_candidate() got num_to_test of " +
            f"{num_to_test}.  num_to_test must be a whole number that is " +
            "zero or greater.")
    if (type(num_to_test) is not int):
        raise TypeError("is_prime_candidate() got a bad type for num_to_test." +
            "  This parameter must be an integer that is greater than or " + 
            "equal to zero.")
        
    # Handle < 4 as a special case
    if (num_to_test < 4):
        return True
    
    # Now down to business!
    result = num_to_test % 6
    if (result == 1 or result == 5):
        return True
    else:
        return False

def main():
    MAX_NUM_TO_TEST = 100
    
    for num_to_test in range(MAX_NUM_TO_TEST + 1):
        if (is_prime_candidate(num_to_test) == True):
            result = prime.is_prime(num_to_test)
            if (result == "prime"):
                print(f"{num_to_test} is PRIME")
            elif (result == "composite"):
                print(f"{num_to_test} is COMPOSITE")
            else:
                print (f"{num_to_test} is NEITHER")
        else:
            print(f"{num_to_test} is COMPOSITE")
            
    print()
    print(f"Tested numbers 0 through {MAX_NUM_TO_TEST}.")
    
#  Everything from here on out is unit testing stuff.  See 
#  https://realpython.com/python-unittest/#using-unittest-from-the-command-line
#  for details.  Here we are doing the version where if you execute this
#  module, it will run the unit tests.  There's also a command-line unit test
#  execution option which we're not using here.  Do note that we imported 
#  unittest up top.

class TestIs_Prime_Candidate(unittest.TestCase):
    # This class contains unit tests for is_prime_candidate.
    
    def test_is_prime_candidate_true(self):
        self.assertEqual(is_prime_candidate(0), True)
        self.assertEqual(is_prime_candidate(1), True)
        self.assertEqual(is_prime_candidate(2), True)
        self.assertEqual(is_prime_candidate(3), True)
        self.assertEqual(is_prime_candidate(5), True)
        self.assertEqual(is_prime_candidate(7), True)
        self.assertEqual(is_prime_candidate(59), True)
        self.assertEqual(is_prime_candidate(61), True)
        
    def test_is_prime_candidate_false(self):
        self.assertEqual(is_prime_candidate(8), False)
        self.assertEqual(is_prime_candidate(9), False)
        self.assertEqual(is_prime_candidate(10), False)
        self.assertEqual(is_prime_candidate(56), False)
        self.assertEqual(is_prime_candidate(57), False)
        self.assertEqual(is_prime_candidate(58), False)
        self.assertEqual(is_prime_candidate(62), False)
        self.assertEqual(is_prime_candidate(63), False)
        self.assertEqual(is_prime_candidate(64), False)
        
    def test_is_prime_ValueError(self):
        with self.assertRaises(ValueError):
            is_prime_candidate(-3)
        with self.assertRaises(ValueError):
            is_prime_candidate(-1)
            
    def test_is_prime_TypeError(self):
        with self.assertRaises(TypeError):
            is_prime_candidate("five")
        with self.assertRaises(TypeError):
            is_prime_candidate("5.5")
        with self.assertRaises(TypeError):
            is_prime_candidate([5])

#----------------------------------------------------------
# Comment out one of the if's below depending on whether you want to run unit 
# tests for this module or run the program itself.  (Or leave them both 
# uncommented and do both!)

# This runs the program
if __name__ == "__main__":
    main()

# This runs the unit tests
if __name__ == "__main__":
    unittest.main(verbosity = 2)