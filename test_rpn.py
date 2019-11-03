import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_sub(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2, result)
    def test_mul(self):
        result = rpn.calculate('12 8 *')
        self.assertEqual(96, result)
    def test_div(self):
        result = rpn.calculate('12 8 /')
        self.assertEqual(1, result)
    def test_div2(self):
        result = rpn.calculate('24 3 /')
        self.assertEqual(8, result)
    
