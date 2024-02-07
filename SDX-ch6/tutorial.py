import math

import unittest

def is_prime(num):
    '''Check if num is prime or not.'''
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True


class TestPrime(unittest.TestCase):

    def test_11(self):
        self.assertTrue(is_prime(11))
    def test_12(self):
        self.assertFalse(is_prime(12))
    def test_1(self):
        self.assertTrue(is_prime(1))
    def test_string(self):
        with self.assertRaises(TypeError):
            is_prime("string")
    def test_negative(self):
        with self.assertRaises(ValueError):
            is_prime(-4)

if __name__ == "__main__":
    unittest.main()



# print(is_prime(12))

# print(is_prime(1))

# assert is_prime(11) == False