import cmath
import time
import sys

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

def test_sign_complex():
    assert sign(complex(5,3)) == 1

def test_sign_float():
    assert sign(1.5) == 1

def test_sign_fraction():
    assert sign(1/5) == 1

# [run]
def run_tests(func_prefix):
    results = {"pass": 0, "fail": 0, "error": 0}
    setup = None
    teardown = None
    isSetup = False
    if ('setup', setup) in globals().items():
        setup()
        isSetup = True

    for (name, test) in globals().items():
        if not name.startswith(func_prefix):
            

            continue
        try:
            start = time.time()
            test()
            end = time.time()
            elapsed = end - start
            print(name + " took " + str(elapsed) + " to run")
            print(name + " passed")
            results["pass"] += 1

        except AssertionError:
            print(name + " failed")
            results["fail"] += 1
        except Exception:
            print(name + " error")
            results["error"] += 1
    print(f"pass {results['pass']}")
    print(f"fail {results['fail']}")
    print(f"error {results['error']}")
    if isSetup:
        teardown()
# [/run]

if len(sys.argv) != 2:
    print("Commands missing, Please run -s <prefix>")
    exit(1)
if (sys.argv[1] == '-s' or sys.argv[1] == '--select'):
    start = time.time()
    run_tests(sys.argv[2])
    end = time.time()
    elapsed = end - start
    print("run_tests took " + str(elapsed) + " to run")
else:
    print("Please run -s <prefix>")
