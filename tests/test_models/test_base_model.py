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

    def test_same_id(self):
        bm = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm.id, bm2.id)

    def test_tim(self):
        bm = BaseModel()
        c = bm.created_at
        u = bm.updated_at
        bm.save()
        self.assertEqual(bm.created_at, c)
        self.assertNotEqual(bm.updated_at, u)

    def test_(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, bm.updated_at)

if __name__ == '__main__':
    unittest.main()
