"""Unit Tests"""
import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """unit tests for methods."""
    def test_english_to_french(self):
        """unit test eng to french"""
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertNotEqual(english_to_french('Bonjour'), 'Hello')

    def test_french_to_english(self):
        """unit test french to english"""
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertNotEqaul(french_to_english('Hello'),'Bonjour')

