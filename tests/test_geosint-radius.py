"""
@author: hogledd
@date: 10/08/18

"""

import unittest
import subprocess


class MyTestCase(unittest.TestCase):
    def setup(self):
        pass

    def test_get_search_radius(self):
        self.assertEqual(
            subprocess.check_output(['python3', 'geosint-radius.py',
                                     '--source', 'https://readexifdata.com/examples/Example%20Niagara%20Falls.JPG',
                                     '--transport', 'car']),
            b'746865206b696420646f6e277420706c6179\n')


if __name__ == '__main__':
    unittest.main()
