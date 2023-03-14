"""Program"""
import re


def find_word(text: str, word: str) -> dict:
    """find word"""
    result = False
    result_find = re.search(word, text)
    if result_find:
        result = True
        index = result_find.span()
    else:
        index = (None, None)
    return {
        'result': result,
        'first_index': index[0],
        'last_index': index[1],
        'search_string': word,
        'string': text
    }


print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming \
                language, and first released it in 1991 as Python 0.9.0.", "Sasha"))
