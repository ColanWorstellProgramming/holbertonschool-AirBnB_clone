#!/usr/bin/python3
"""tests"""
import unittest
from models.review import Review


class TestReviewModel(unittest.TestCase):
    """tests"""
    def test_init(self):
        self.assertEqual(Review, type(Review()))

    def test_review_pid(self):
        sd = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(Review()))
        self.assertNotIn("place_id", sd.__dict__)

    def test_review_uid(self):
        sd = Review()
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(Review()))
        self.assertNotIn("user_id", sd.__dict__)


if __name__ == "__main__":
    unittest.main()
