# CYRILLIC_SYMBOLS = [ord(symbol) for symbol in "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"]
# TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
#                "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

# TRANS = dict(zip(CYRILLIC_SYMBOLS, TRANSLATION))


# def translate(name):
#     return name.translate(TRANS)


# print(translate("ДДДДДдддмитро Короб"))  # Dmitro Korob
# print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk


##############################################################################################

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

print(zip(CYRILLIC_SYMBOLS, TRANSLATION))

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def translate(name):
    return name.translate(TRANS)


print(translate("Дмитро Короб"))  # Dmitro Korob
print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk
