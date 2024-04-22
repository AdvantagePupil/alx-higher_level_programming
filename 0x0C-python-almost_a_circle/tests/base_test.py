#!/usr/bin/python3
"""Unittests for base
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Define unit test for Base model"""

    def setUp(self):
        """Set up test instances before each test method."""
        self.base1 = Base()
        self.base2 = Base()
        self.base_with_id = Base(100)

    def test_initialization(self):
        """Test Base model initialization."""
        self.assertEqual(self.base1.id, 1)
        self.assertEqual(self.base2.id, 2)

    def test_saving_id(self):
        """Test saving id in Base model."""
        self.assertEqual(self.base_with_id.id, 100)

    def test_to_json_string_valid(self):
        """Placeholder for testing to_json_string method."""
        pass

if __name__ == '__main__':
    unittest.main()
