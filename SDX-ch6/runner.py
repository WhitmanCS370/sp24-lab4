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
    assert sin(1) == 1

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



def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    errors = {"error": [], "fail": [], "pass": []}

    for (name, test) in globals().items():
        if name == "setup": 
                setup()
        if name == "teardown":
            teardown = name

    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            test()
            results["pass"] += 1
            errors["pass"].append(name)
        except AssertionError:
            results["fail"] += 1
            errors["fail"].append(name)
        except Exception:
            results["error"] += 1
            errors["error"].append(name)

    if teardown:
        teardown()
    print(f"pass {results['pass']}, {errors['pass']}")
    print(f"fail {results['fail']}, {errors['fail']}")
    print(f"error {results['error']}, {errors['error']}")

def setup():
    pass

def teardown():
    pass



if __name__ == "__main__":
    unittest.main()
    run_tests()