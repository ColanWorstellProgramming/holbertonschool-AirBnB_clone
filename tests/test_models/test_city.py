#!/usr/bin/python3
"""tests"""
import unittest
from models.city import City


class TestCityModel(unittest.TestCase):
    """tests"""
    def test_init(self):
        self.assertEqual(City, type(City()))

    def test_sta_id(self):
        ct = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(ct))
        self.assertNotIn("state_id", ct.__dict__)

if __name__ == "__main__":
    unittest.main()
