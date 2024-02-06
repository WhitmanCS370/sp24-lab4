import unittest
import time

from sign_func import sign
# unittest must import what we want to test, can't be in the same file (like pytest).

# pytest has boolean stuff, unittest is one function/method, more concise.

class TestCase(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()
        self.currentTime = time.time()
        # we don't really have anything to set up
        print("setUp called! " + str(self.startTime))

    def tearDown(self):
        # we also don't have anything to tear down
        print(self.currentTime)
        print(self.currentTime - self.startTime)

    def test_sign_negative(self):
        self.currentTime = time.time()
        self.assertEqual(-1,sign(-3))

    def test_sign_positive(self):
        self.currentTime = time.time()
        self.assertEqual(1,sign(19))

    def test_sign_zero(self):
        self.currentTime = time.time()
        self.assertTrue(1,sign(0))

    def test_sign_error(self):
        self.currentTime = time.time()
        with self.assertRaises(AssertionError):
            self.assertFalse(1,sign(1))

if __name__ == '__main__':
    unittest.main(verbosity=2)


'''
# [run]
def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            TestCase()
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