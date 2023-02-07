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

    def test_save(self):
        bm = BaseModel()
        self.file_storage.new(bm)
        self.file_storage.save()
        with open(self.file_path, "r") as file:
            file_content = json.load(file)
        self.assertEqual(bm.to_dict(),
                         file_content["BaseModel.{}".format(bm.id)])

    def test_reload(self):
        bm = BaseModel()
        self.file_storage.new(bm)
        self.file_storage.save()
        self.file_storage.__objects = {}
        self.file_storage.reload()
        objects = self.file_storage.all()
        self.assertEqual(bm.to_dict(),
                         objects["BaseModel.{}".format(bm.id)].to_dict())

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

if __name__ == "__main__":
    unittest.main()
