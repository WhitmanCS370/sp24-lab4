import unittest
import pytest

from manual import sign

class TestSign(unittest.TestCase):
    def test_negThree(self):
        self.assertEqual(sign(-3), -1)
    def test_nineteen(self):
        self.assertEqual(sign(19), 1)
    def test_zero(self):
        self.assertEqual(sign(0), 0)


def test_sign_negThree():
    # Given
    x = -3
    assert sign(x) == -1

def test_sign_nineteen():
    x = 19
    assert sign(19) == 19

def test_sign_zero():
    x = 0
    assert sign(0) == 0

def run_tests():
    test_sign_negThree()
    test_sign_nineteen()
    test_sign_zero()

if __name__ == '__main__':
    unittest.main()
    