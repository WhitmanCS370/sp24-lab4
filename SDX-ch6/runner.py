import time

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
def run_tests():
    start = time.time()
    failed_tests = []
    errored_tests = []
    results = {"pass": 0, "fail": 0, "error": 0}
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            test()
            results["pass"] += 1
        except AssertionError:
            results["fail"] += 1
            failed_tests.append(name)
        except Exception:
            results["error"] += 1
            errored_tests.append(name)
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    if len(failed_tests) > 0:
        print(failed_tests)
    print(f"error {results['error']}")
    if len(errored_tests) > 0:
        print(errored_tests)
    end = time.time()
    numTests = results["pass"] + results["error"] + results["fail"]
    elapsed = end - start
    print(str(numTests) + " tests ran in " + str(elapsed) + " seconds.")
# [/run]

run_tests()
