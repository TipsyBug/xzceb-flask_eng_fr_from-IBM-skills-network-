import unittest
from translator import english_to_french
from translator import french_to_english

class MyTest(unittest.TestCase):

    def test_e2f(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_f2e(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()