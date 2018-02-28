# encoding: utf-8
'''
@author: zhushen
@contact: 810909753@q.com
@time: 2018/2/28 13:09
'''
import unittest


def division_funtion(x, y):
    return x / y


class TestDivision(unittest.TestCase):
    def test_int(self):
        self.assertEqual(division_funtion(9, 3), 3)

    def test_int2(self):
        self.assertEqual(division_funtion(9, 4), 2.25)

    def test_float(self):
        self.assertEqual(division_funtion(4.2, 3), 1.4)


if __name__ == '__main__':
    unittest.main()
    
    