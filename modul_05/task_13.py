"""Тепер ми потренуємося писати корисні регулярні вирази. Напишіть регулярний вираз для функції 
find_all_emails, яка буде в тексті (параметр text) знаходити всі email та повертати список отриманих 
з тексту збігів."""

import re


def find_all_emails(text):
    """find all emails"""
    result = re.findall(r"[a-zA-Z][a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}", text)
    return result
