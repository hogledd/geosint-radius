"""
@author: hogledd
@date: 11/08/18

"""

import unittest
import utils


class MyTestCase(unittest.TestCase):
    def setup(self):
        pass

    def test_check_valid_URL(self):
        self.assertEqual(utils.check_valid_URL('https://www.instagram.com'), True)


if __name__ == '__main__':
    unittest.main()
