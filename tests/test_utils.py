"""
@author: hogledd
@date: 11/08/18

"""

import unittest
import utils

class MyTestCase(unittest.TestCase):
    def setup(self):
        pass

    def test_checkValidUrl(self):
        self.assertEqual(utils.checkValidURL('https://www.instagram.com'), True)

if __name__ == '__main__':
    unittest.main()
