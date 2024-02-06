import unittest

from sign_func import sign
# unittest must import what we want to test, can't be in the same file (like pytest).

# pytest has boolean stuff, unittest is one function/method, more concise.

    
class TestCade(unittest.TestCase):
    def test_sign_negative(self):
        self.assertEqual(-1,sign(-3))

    def test_sign_positive(self):
        self.assertEqual(1,sign(19))

    def test_sign_zero(self):
        self.assertEqual(1,sign(0))

    def test_sign_error(self):
        self.assertFalse(1,sign(1))

if __name__ == '__main__':
    unittest.main()


# [run]
    '''
        def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
        except Exception:
            results["error"] += 1
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")
# [/run]

run_tests()
'''