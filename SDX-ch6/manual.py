import unittest

# [sign]
def sign(value):
    if value < 0:
        return -1
    else:
        return 1
# [/sign]

# [tests]
def test_sign_negative():
    assert sign(-3) == -1

def test_sign_positive():
    assert sign(19) == 1
 
def test_sign_zero():
    assert sign(0) == 0

def test_sign_error():
    assert sgn(1) == 1
# [/tests]
    
class TestManual(unittest.TestCase):
    def test_sign_negative(self):
        self.assertTrue(sign(-3))
    def test_sign_positive(self):
        self.assertTrue(sign(19))
    def test_sign_zero(self):
        self.assertTrue(sign(0))
    def test_sign_error(self):
        self.assertTrue(sgn(1))

if __name__ == '__main__':
    unittest.main()

# [run]
def run_tests(all_tests):
    results = {"pass": 0, "fail": 0, "error": 0}
    for test in all_tests:
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

# [use]
TESTS = [
    test_sign_negative,
    test_sign_positive,
    test_sign_zero,
    test_sign_error
]

run_tests(TESTS)
# [/use]
