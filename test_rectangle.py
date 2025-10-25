
import unittest

from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(3, 3), 9)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(0, 10), 20)
        self.assertEqual(perimeter(3, 3), 12)






