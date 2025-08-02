# test_hyperdata.py
"""
Tests for HyperData module.
"""

import unittest
from hyperdata import HyperData

class TestHyperData(unittest.TestCase):
    """Test cases for HyperData class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HyperData()
        self.assertIsInstance(instance, HyperData)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HyperData()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
