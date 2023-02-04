#!/usr/bin/python3
"""unit tests"""


import unittest
import uuid

from models.base_model import BaseModel
from datetime import datetime

class BaseModelTestsQuestionFour(unittest.TestCase):
    """unit test for BaseModel class"""
    def test_id(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_exist(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_update(self):
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_dict(self):
        bm = BaseModel()
        dc = bm.to_dict()
        self.assertIsInstance(dc, dict)
        self.assertIsInstance(dc["updated_at"], str)
        self.assertIsInstance(dc["created_at"], str)

if __name__ == '__main__':
    unittest.main()
