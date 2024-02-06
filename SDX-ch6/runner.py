import sys
import time

def setup():
    print("setting up")

def teardown():
    print("tearing down")

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
    assert sig(1) == 1

# [run]
def run_tests(pattern=None):
    total_start_time = time.time()
    # add *args and **kwargs if you need to pass arguments
    if "setup" in globals():
        globals()["setup"]()

    results = {"pass": [], "fail": [], "error": []}
    for (name, test) in globals().items():
        if not name.startswith("test_") or (pattern is not None and pattern not in name):
            continue
        start_time = time.time()
        try:
            test()
            results["pass"].append(name)
        except AssertionError:
            results["fail"].append(name)
        except Exception:
            results["error"].append(name)
        end_time = time.time()
        print(f"{name} run time: {end_time - start_time:.8f}")

    print(f"pass: {', '.join(results['pass'])} - number: {len(results['pass'])}")
    print(f"fail: {', '.join(results['fail'])} - number: {len(results['fail'])}")
    print(f"error: {', '.join(results['error'])} - number: {len(results['error'])}")
    total_end_time = time.time()
    print(f"Total test time: {total_end_time - total_start_time:.8f}")

    if "teardown" in globals():
        globals()["teardown"]()
    
    return results

# [/run]

if len(sys.argv) > 2 and (sys.argv[1] == "-s" or sys.argv[1] == "--select"):
    run_tests(sys.argv[2])
elif len(sys.argv) > 1 and (sys.argv[1] == "-t" or sys.argv[1] == "--test"):
    results = run_tests()
    assert (len(results["pass"]) == 2 and len(results["fail"]) == 1 and len(results["error"]) == 1)
else:
    run_tests()


