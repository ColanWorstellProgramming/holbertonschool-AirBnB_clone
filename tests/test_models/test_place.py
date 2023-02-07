#!/usr/bin/python3
"""tests"""
import unittest
from models.place import Place


class TestPlaceModel(unittest.TestCase):
    """tests"""
    def test_init(self):
        self.assertEqual(Place, type(Place()))

    def test_cid(self):
        pl = Place()
        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(pl))
        self.assertNotIn("city_id", pl.__dict__)

    def test_up(self):
        pl = Place()
        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(pl))
        self.assertNotIn("user_id", pl.__dict__)


if __name__ == "__main__":
    unittest.main()
