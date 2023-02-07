#!/usr/bin/python3
"""storage tests"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """file storage tests"""

    def setUp(self):
        self.file_storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path

    def test_all(self):
        bm = BaseModel()
        self.file_storage.new(bm)
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)
        self.assertEqual(bm, objects["BaseModel.{}".format(bm.id)])

    def test_new(self):
        bm = BaseModel()
        self.file_storage.new(bm)
        objects = self.file_storage.all()
        self.assertEqual(bm, objects["BaseModel.{}".format(bm.id)])

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

if __name__ == "__main__":
    unittest.main()
