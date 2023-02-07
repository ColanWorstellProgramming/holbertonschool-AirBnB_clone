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
        self.assertNotEqual(bm.id, bm2.id)

    def test_met(self):
        bm = BaseModel()
        self.assertIn(bm.id, str(bm))

    def test_with_kwargs(self):
        created_at = '2023-04-20T00:00:00.000000'
        updated_at = '2023-04-20T00:00:00.000000'
        moby = {
            'id': 'villager',
            'created_at': created_at,
            'updated_at': updated_at,
            'name': 'uwu'
        }
        bm1 = BaseModel(**moby)
        self.assertEqual(bm1.id, 'villager')
        self.assertEqual(bm1.created_at,
                         datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm1.updated_at,
                         datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(bm1.name, 'uwu')


if __name__ == '__main__':
    unittest.main()
