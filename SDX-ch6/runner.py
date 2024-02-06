# Improved complete runner using a testing class inheriting from the unittest module
import unittest
from sign import sign


class TestClass(unittest.TestCase):
    def test_sign_negative(self):
        self.assertEqual(-1, sign(-3))

    def test_sign_positive(self):
        self.assertEqual(1, sign(19))

    def test_sign_zero(self):
        self.assertEqual(1, sign(0))

    def test_sign_error(self):
        self.assertEqual(1, sign(1))

    def test_exception(self):
        with self.assertRaises(TypeError):
            sign('0') 

if __name__ == '__main__':
    unittest.main()