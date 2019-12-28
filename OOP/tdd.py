import unittest

def reverseList(to_reverse):
  if type(to_reverse) is list:
    return to_reverse[::-1]
  return None

class ReverseListTestCase(unittest.TestCase):

  def testEmpty(self):
    self.assertEqual(reverseList([]), [])

  def testOne(self):
    self.assertEqual(reverseList([1]), [1])

  def testReversed(self):
    self.assertEqual(reverseList([1,3,5]), [5,3,1])

if __name__ == '__main__':
    unittest.main()
