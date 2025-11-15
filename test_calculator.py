import unittest
from calculator import *

# https://github.com/Isabella6767/lab11-IV-NA

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(3, 4),7)

    def test_subtract(self):
         self.assertEqual(calculator.subtract(10, 3), 7)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5,0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithe(10, 100), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithe(1,10)

    def test_multiple(self):
        self.assertEqual(calculator.multiple(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(8, 2), 4)

    def test_log_invalid_arguemnt(self):
        with self.assertRaises(ValueError):
            calculator.logarith(1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3)

    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()


