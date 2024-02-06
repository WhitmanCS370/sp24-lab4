import time, sys

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

def setup():
    pass

def teardown():
    pass

# [run]
def run_tests():
    results = {"pass": 0, "fail": 0, "error": 0}
    if ('setup', setup) in globals().items():
        setup()
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        try:
            startTime = time.time()
            test()
            endTime = time.time()
            elapsedTime = endTime - startTime
            results["pass"] += 1
            print("time elapsed: ", elapsedTime)
            print(name, "test passed")
        except AssertionError:
            endTime = time.time()
            elapsedTime = endTime - startTime
            results["fail"] += 1
            print("time elapsed: ", elapsedTime)
            print(name, "test failed")
        except Exception:
            endTime = time.time()
            elapsedTime = endTime - startTime
            results["error"] += 1
            print("time elapsed: ", elapsedTime)
            print(name, "test generated error")
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")
    if ('teardown', teardown) in globals().items():
        teardown()
# [/run]

run_tests()
