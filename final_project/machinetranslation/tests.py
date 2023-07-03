import unittest
from translator import english_to_french, french_to_english


class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test_e2f(self):
        """Test Hello returns Bonjour"""
        self.assertEqual(english_to_french('hello'), 'bonjour')
        """Test Hello doesn't return Bonjour"""
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test_f2e(self):
        """Test Bonjour returns Hello"""
        self.assertEqual(french_to_english('bonjour'), 'hello')
        """Test Bonjour doesn't return Hello"""    
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')

if __name__ == "__main__":
    unittest.main()
