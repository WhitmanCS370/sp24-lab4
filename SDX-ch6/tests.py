import unittest
import time

from find_test_funcs import sign

import sys
argvlen = len(sys.argv)

class CustomTestResult(unittest.TestResult):
    def startTest(self, test):
        super().startTest(test)
        self._test_start_time = time.time()

    def stopTest(self, test):
        super().stopTest(test)
        duration = time.time() - self._test_start_time
        print(f"{test.id()} - Time taken: {duration:.6f} seconds")

class TestSign(unittest.TestCase):

    def test_sign_negative(self):
        self.assertEqual(sign(-3), -1)
        
    def test_sign_positive(self):
        self.assertEqual(sign(19), 1)
        
    def test_sign_zero(self):
        self.assertEqual(sign(0), 0)
        
    def test_sign_error(self):
        with self.assertRaises(ValueError):
            sgn(1)

def run_test(args = [""]):
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSign)
    result = CustomTestResult()
    suite.run(result)
    print(f"Pass Count: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Fail Count: {len(result.failures)}")
    print(f"Error Count: {len(result.errors)}")


if argvlen > 2 and (sys.argv[1] == '-s' or sys.argv[1] == "--select"):
    run_test(sys.argv[2])
else:
    run_test()


