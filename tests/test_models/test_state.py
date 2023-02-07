#!/usr/bin/python3
"""tests"""
import unittest
from models.state import State


class TestStateModel(unittest.TestCase):
    """tests"""
    def test_init(self):
        self.assertEqual(State, type(State()))

    def test_state_name(self):
        st = State()
        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(State()))
        self.assertNotIn("name", st.__dict__)

if __name__ == "__main__":
    unittest.main()
