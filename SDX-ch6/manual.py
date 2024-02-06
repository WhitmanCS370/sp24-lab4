import unittest

# [sign]
def sign(value):
     # raise TypeError for invalid input type
    if type(value) != int:
        raise TypeError('value is of invalid type')
    if value < 0:
        return -1
    else:
        return 1
# [/sign]

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