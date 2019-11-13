## Reference: https://realpython.com/python-testing/#choosing-a-test-runner

import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def setUp(self):
        print("This method is called on the start of every test")

    def tearDown(self):
        print("This method is called on the end of every test")

    def test(self):
        self.assertEqual(fun(3), 4)

    def testFailed(self):
        self.assertEqual(fun(3), 6)

if __name__ == "__main__":
    unittest.main()
