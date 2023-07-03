"""
This module provides functions to translate languages

Author: Anatoly Gladky
Date: 06.29.2023
"""


from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function takes the English text as input
    and returns the French translation as output.
    """

    french_text = MyMemoryTranslator(source='en-EN', target='fr-FR').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function takes the French text as input
    and returns the English translation as output.
    """

    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
