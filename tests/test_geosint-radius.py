"""
@author: hogledd
@date: 10/08/18

"""

import unittest
import subprocess

class MyTestCase(unittest.TestCase):
    def setup(self):
        pass

    def test_getSearchRadius(self):
        self.assertEqual(
            subprocess.check_output(['python3', 'geosint-radius.py',
                                     '--source', '1c0111001f010100061a024b53535009181c',
                                     '--trasnport', 'car']),
            b'746865206b696420646f6e277420706c6179\n')

if __name__ == '__main__':
    unittest.main()
