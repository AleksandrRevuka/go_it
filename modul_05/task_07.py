def normalize(name: str) -> str:
    """Converts Cyrillic to Latin and assigns characters to '_'."""

    cyrillic_symbols = CYRILLIC_SYMBOLS + CYRILLIC_SYMBOLS.upper()
    cyrillic_symbols_all = [ord(symbol) for symbol in cyrillic_symbols]
    translation = TRANSLATION + [symbol.upper() for symbol in TRANSLATION]
    trans = dict(zip(cyrillic_symbols_all, translation))

    return name.translate(trans)

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ["a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"]

print(normalize("ДДДДДдддмитро Короб"))  # Dmitro Korob
print(normalize("Олекса Івасюк"))  # Oleksa Ivasyuk


##############################################################################################


# print(zip(CYRILLIC_SYMBOLS, TRANSLATION))

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    return name.translate(TRANS)


print(translate("Дмитро Короб"))  # Dmitro Korob
print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk
