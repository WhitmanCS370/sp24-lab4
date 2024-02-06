import unittest
# [sign]
def sign(value):
    if value < 0:
        return -1
    else:
        return 1
# [/sign]

class TestSign(unittest.TestCase):


# [tests]
    def test_sign_negative(self):
        self.assertEqual(sign(-3) , -1)
    #assert sign(-3) == -1

    def test_sign_positive(self):
        self.assertEqual(sign(19), 1)
    #assert sign(19) == 1

    def test_sign_zero(self):
    #assert sign(0) == 0
        self.assertEqual(sign(0), 0)

    def test_sign_error(self):
    #assert sgn(1) == 1
        self.assertEqual(sign(1),1)
# [/tests]

# [run]
""" 
 def run_tests(TestSign):
    results = {"pass": 0, "fail": 0, "error": 0}
    for test in TestSign:
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
"""


# [use]
"""TESTS = [
    test_sign_negative,
    test_sign_positive,
    test_sign_zero,
    test_sign_error
]

#run_tests(TESTS)
# [/use]
"""
#chatgbt helped with run_test because we couldnt find our error

def run_tests(TestSign):
    # Instantiate the TestSign class
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestSign)
    # Run the tests
    test_runner = unittest.TextTestRunner()
    test_result = test_runner.run(test_suite)

    # Retrieve and print the test results
    print(f"Pass: {test_result.testsRun - len(test_result.failures) - len(test_result.errors)}")
    print(f"Fail: {len(test_result.failures)}")
    print(f"Error: {len(test_result.errors)}")
# [/run]

# [use]
if __name__ == "__main__":
    run_tests(TestSign)
