"""Program for translation."""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """Translate English to French."""
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """Translate French to English."""
    english_text = MyMemoryTranslator(source='en', target='fr').translate(french_text)
    return english_text
