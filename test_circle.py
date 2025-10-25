import unittest
from circle import area, perimeter
class CircleTestCase(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(area(5), 78.53981633974483)
        self.assertEqual(area(10), 314.1592653589793)
        self.assertEqual(area(3), 28.274333882308138)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(10), 62.83185307179586)
        self.assertEqual(perimeter(3), 18.84955592153876)
        