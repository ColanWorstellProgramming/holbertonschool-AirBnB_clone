#!/usr/bin/python3
"""tests"""
import unittest
from models.user import User


class TestUserModel(unittest.TestCase):
    """tests"""
    def test_init(self):
        self.assertEqual(User, type(User()))

    def test_email_pub(self):
        self.assertEqual(str, type(User.email))

    def test_paswd_pub(self):
        self.assertEqual(str, type(User.password))

    def test_fname_pub(self):
        self.assertEqual(str, type(User.first_name))

    def test_lname_pub(self):
        self.assertEqual(str, type(User.last_name))


if __name__ == "__main__":
    unittest.main()
