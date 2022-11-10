import unittest
import sys
sys.path.append('../')
import translator

class TestEnglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        """
        Test that it can translate from english to French.
        """
        
        self.assertIsNotNone(translator.english_to_french('Hello'))

    def test_frenchToEnglish(self):
        """
        Test that it can translate from French to English.
        """
        self.assertIsNotNone(translator.french_to_english('Bonjour'))

if __name__ == '__main__':
    unittest.main()

