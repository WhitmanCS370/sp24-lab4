import unittest

def sign(value):
    if value < 0:
        return -1
    else:
        return 1

def test_sign_negative():
    assert sign(-3) == -1

def test_sign_positive():
    assert sign(19) == 1

def test_sign_zero():
    assert sign(0) == 0

def test_sign_error():
    assert sign(1) == 1

# [run]
class TestCase(unittest.TestCase):
    def test_sign_negative(self):
        self.assertEqual(sign(-3),-1)

    def test_sign_positive(self):
        self.assertEqual(sign(19),1)

    def test_sign_zero(self):
        self.assertEqual(sign(0),0)

    def test_sign_error(self):
        self.assertEqual(sign(1),1)


# Test.test_sign_error()
# Test.test_sign_negative()
# Test.test_sign_positive()
# Test.test_sign_zero()

def runtests():
    Test=TestCase()
    unittest.main()

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
runtests()
