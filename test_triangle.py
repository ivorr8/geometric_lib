import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5, 10), 25)
        self.assertEqual(area(10, 10), 50)
        self.assertEqual(area(3, 4), 6)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 10, 4), 19)
        self.assertEqual(perimeter(6, 10, 5), 21)
        self.assertEqual(perimeter(3, 3, 6), 12)