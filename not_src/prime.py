# -*- coding: utf-8 -*-
"""
prime.py - figuring out how to use the unittest and logger built-in libraries 
by incorporating them into a prime number finding program.
"""

import math
import unittest

def is_prime(num_to_test):
    """
    Accepts an integer num_to_test and returns a string - either "prime", 
    "composite", or "neither" depending on num_to_test.  Uses brute force
    along with the observation that when testing divisors against num_to_test, 
    it's not necessary to go any higher than sqrt(num_to_test)

    """
    # Input checking
    if (num_to_test < 0):
        raise ValueError("prime.is_prime() got num_to_test of " +
            f"{num_to_test}.  num_to_test must be a whole number that is " +
            "zero or greater.")
    if (type(num_to_test) is not int):
        raise TypeError("prime.is_prime() got a bad type for num_to_test." +
            "  This parameter must be an integer that is greater than or " + 
            "equal to zero.")
    
    # Handle num_to_test = 0, 1, 2, and 3 as special cases
    if (num_to_test == 0 or num_to_test == 1):
        return "neither"
    if (num_to_test == 2 or num_to_test == 3):
        return "prime"

    # Time to do the actual work!
    greatest_divisor_to_test = math.sqrt(num_to_test)
    divisor_to_test = 2
    
    while(True):
        if (num_to_test % divisor_to_test == 0):
            return "composite"
        divisor_to_test = divisor_to_test + 1
        if (divisor_to_test > greatest_divisor_to_test):
            break
        
    return "prime"
    
#  Everything from here on out is unit testing stuff.  See 
#  https://realpython.com/python-unittest/#using-unittest-from-the-command-line
#  for details.  Here we are doing the version where if you execute this
#  module, it will run the unit tests.  There's also a command-line unit test
#  execution option which we're not using here.  Do note that we imported 
#  unittest up top.

class TestIs_Prime(unittest.TestCase):
    # This class contains unit tests for is_prime.
    
    def test_is_prime_neither(self):
        self.assertEqual(is_prime(0), "neither")
        self.assertEqual(is_prime(1), "neither")
        
    def test_is_prime_composite(self):
        self.assertEqual(is_prime(4), "composite")
        self.assertEqual(is_prime(6), "composite")
        self.assertEqual(is_prime(15), "composite")
        self.assertEqual(is_prime(100), "composite")
        self.assertEqual(is_prime(999), "composite")
        
    def test_is_prime_prime(self):
        self.assertEqual(is_prime(2), "prime")
        self.assertEqual(is_prime(3), "prime")
        self.assertEqual(is_prime(5), "prime")
        self.assertEqual(is_prime(11), "prime")
        self.assertEqual(is_prime(43), "prime")
        
    def test_is_prime_ValueError(self):
        with self.assertRaises(ValueError):
            is_prime(-3)
        with self.assertRaises(ValueError):
            is_prime(-1)
            
    def test_is_prime_TypeError(self):
        with self.assertRaises(TypeError):
            is_prime("five")
        with self.assertRaises(TypeError):
            is_prime("5.5")
        with self.assertRaises(TypeError):
            is_prime([5])

if __name__ == "__main__":
    unittest.main(verbosity = 2)