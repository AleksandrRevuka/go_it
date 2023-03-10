articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark Gun",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    result = []
    for article in articles_dict:
        for value in article.values():
            if letter_case:
                if key in str(value):
                    result.append(article)
            else:
                if key.lower() in str(value).lower():
                    result.append(article)

    return result


print(find_articles("gun", letter_case=False))
