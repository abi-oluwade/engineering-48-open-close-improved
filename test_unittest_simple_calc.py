import unittest # unittest is a LIBRARY
from simple_calc import SimpleCalc # we do not currently have this {file} or this {class}.

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 4), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3, 6))

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)