#!/usr/bin/python3
"""tests"""
import unittest
from models.amenity import Amenity


class TestAmenityModel(unittest.TestCase):
    """tests"""
    def test_init(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_name_pub(self):
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)


if __name__ == "__main__":
    unittest.main()
