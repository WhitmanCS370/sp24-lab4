import unittest

from prime import is_prime

class TestClass(unittest.TestCase):
    def test_1(self):
		# check function_to_test
        self.assertTrue(is_prime(7))
    
    def test_2(self):
		# check function_to_test
        self.assertTrue(7)
    
    def test_3(self):
		# check function_to_test
        pass

    def test_exception(self):
        with self.assertRaises(TypeError):
            is_prime(6)
        with self.assertRaises(ValueError):
            is_prime(-1)
            