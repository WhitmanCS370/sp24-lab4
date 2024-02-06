import unittest
import time

def sign(value):
    if value < 0:
        return -1
    else:
        return 1
  

def setup():
    print("attemped setup")
    return


def teardown():
    print("attemped teardown")
    return


class TestClass(unittest.TestCase):

    
    timeStarted = time.time()
    #print(timeStarted)
    setupFlag = False
    if ("setup" in globals()) and ("teardown" in globals()):
        setupFlag = True
        
    def classSetUp(self):
        if self.setupFlag:
            eval("setup()") # or className.setup() if contained in class
        
    def classTearDown(self):
        if self.setupFlag:
            eval("teardown()")
    
    def recordTimeStarted(self):
        self.timeStarted = time.time()

    def stopTimeRecord(self):
        print("This took ")
        temp = time.time()
        print(temp - self.timeStarted)
        
    def test_sign_negative(self):
        self.recordTimeStarted()
        self.classSetUp()
        self.assertTrue(sign(-3) == -1)
        self.classTearDown()
        self.stopTimeRecord()
	
    def test_sign_positive(self):
        self.classSetUp()
        self.assertTrue(sign(19) == 1)
        self.classTearDown()
	
    def test_sign_zero(self):
        self.classSetUp()
        self.assertTrue(sign(0) == 0)
        self.classTearDown()
        
    
    def test_sign_error(self):
        self.classSetUp()
        self.assertTrue(sign(1) == 1)
        self.classTearDown()
        
    def test_sign_outliers(self):
        with self.assertRaises(TypeError):
            sign("test") #raises an error is this works
    
    
if __name__=='__main__':
    """
    name = None
    for name in globals():
        print(name)
    """
    unittest.main()
    