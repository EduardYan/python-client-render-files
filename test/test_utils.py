"""
This is the test for utils
module.
"""

import sys
sys.path.append('..')

import unittest
from helpers.utils import get_user_name

class TestUtils(unittest.TestCase):
  def setUp(self) -> None:
      print('setUP')

      self.user_example = 'dan'

  def tearDown(self) -> None:
      print('tearDown')

  def test_get_user_name(self):
    print('Testing this function')

    self.assertEqual(self.user_example, get_user_name())

if __name__ == '__main__':
  unittest.main()