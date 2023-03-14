"""write a function find_all_words that searches for a word match in the text"""
import re


def find_all_words(text: str, word: str) -> list:
    """find words in string"""
    return re.findall(word, text, re.IGNORECASE)


print(find_all_words("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming \
                language, and first released it in 1991 as Python 0.9.0.", "python"))
