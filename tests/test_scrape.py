"""
@author: hogledd
@date: 11/08/18

"""

import unittest
import scrape


class MyTestCase(unittest.TestCase):
    def setup(self):
        pass

    def test_get_image_coords(self):
        self.assertEqual(scrape.get_image_coords('https://readexifdata.com/examples/Example%20Niagara%20Falls.JPG'),
                         (43.085166666666666,-79.07983333333334))


if __name__ == '__main__':
    unittest.main()
