import unittest
import sys
sys.path.append('../')
import translator

class TestEnglishToFrench(unittest.TestCase):
    def test_englishToFrench(self):
        """
        Test that it can translate from english to French.
        """
        
        self.assertEqual(translator.english_to_french('Hello'),'Bonjour')

        self.assertNotEqual(translator.english_to_french('Hello'),None)
        

    def test_frenchToEnglish(self):
        """
        Test that it can translate from French to English.
        """
        self.assertEqual(translator.french_to_english('Bonjour'),'Hello')
        self.assertNotEqual(translator.french_to_english('Bonjour'),None)

if __name__ == '__main__':
    unittest.main()

p