# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/3/12 11:10
'''

import unittest
from component.staticmethod import *
from component.variable import get_val, set_val

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    def test_trans_time(self):
        """Test method add(a, b)"""
        self.assertEqual(3, trans_time())
        self.assertNotEqual(3, trans_time())


if __name__ == '__main__':
    unittest.main()