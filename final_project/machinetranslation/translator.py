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

    french_text = MyMemoryTranslator(english_text,"french")
    return french_text

def french_to_english(french_text):
    """
    This function takes the French text as input
    and returns the English translation as output.
    """

    english_text = MyMemoryTranslator(french_text, "english")
    return english_text

# fr = english_to_french("Hello")
# print("French translation is ", fr)
