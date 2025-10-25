import unittest
from square import area, perimeter
class SquareTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(30), 900)
        self.assertEqual(area(3), 9)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(10), 40)
        self.assertEqual(perimeter(3), 12)