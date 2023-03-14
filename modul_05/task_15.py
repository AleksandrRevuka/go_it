"""Напишіть регулярний вираз для функції find_all_links, яка буде в тексті (параметр text) 
знаходити всі лінки та повертати список отриманих з тексту збігів."""
import re


def find_all_links(text: str) -> list:
    """find all links"""
    result = []
    iterator = re.finditer(r"https?://(?:[a-z]+\.)+[a-z]{2,}(?![^<>]*>)", text)
    for match in iterator:
        result.append(match.group())
    return result


print(find_all_links( 'The main search site in the world is https://www.google.com The main social network \
                     for people in the world is https://www.facebook.com But programmers have their own social \
                     network http://github.com There they share their code. some url to check https://www..facebook.com \
                     www.facebook.com '))
