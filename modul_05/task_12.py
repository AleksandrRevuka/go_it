"""Напишіть функцію replace_spam_words, яка приймає рядок (параметр text), перевіряє його на вміст 
заборонених слів зі списку (параметр spam_words), та повертає результат рядок, але замість заборонених 
слів, підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. Визначити 
нечутливість до регістру стоп-слів."""

import re


def replace_spam_words(text: str, spam_words: list) -> str:
    """replace spam words"""
    for spam_word in spam_words:
        if re.search(spam_word, text, re.I):
            text = re.sub(spam_word, len(spam_word) * '*', text, flags=re.I)
    return text



print(replace_spam_words("Guido van Rossum fuck began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", ["pyThon", "FuCk"]))
