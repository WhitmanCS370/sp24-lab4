import unittest

class Sign_Test(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(-1, sign(-3))

    def test_positive(self):
        self.assertEqual(1, sign(19))

    def test_zero(self):
        self.assertEqual(1, sign(0))

    def test_error(self):
        with self.assertRaises(NameError):
            sgn(1)

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
    assert sgn(1) == 1

# [run]
def run_tests(test_list):
    results = {"pass": [], "fail": [], "error": []}
    for (name, test) in test_list.items():
        try:
            test()
            results["pass"].append(name)
        except AssertionError:
            results["fail"].append(name)
        except Exception:
            results["error"].append(name)
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")
    return results
# [/run]

def setup():
    # creeate list of functions
    tests = {}
    for(name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        else:
            tests[name] = test
    print(tests)
    return tests

def teardown():
    pass

test_list = setup()
run_tests(test_list)
# unittest.main()