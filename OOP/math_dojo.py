import unittest
from functools import reduce

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num + reduce(lambda x,y: x+y, nums, 0)
        return self

    def subtract(self, num, *nums):
        self.result -= num + reduce(lambda x,y: x+y, nums, 0)
        return self

class MathDojoTestCase(unittest.TestCase):
  def setUp(self):
    self.md = MathDojo()

  def testBase(self):
    x = self.md.add(2).add(2,5,1).subtract(3,2).result
    self.assertEqual(x, 5)

  def testNegative(self):
    x = self.md.add(-2).add(2).result
    self.assertEqual(x, 0)

if __name__ == '__main__':
  unittest.main()
  # create an instance:
  md = MathDojo()
  # to test:
  x = md.add(2).add(2,5,1).subtract(3,2).result
  print(x)
