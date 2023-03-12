# def is_spam_words(text, spam_words, space_around=False):
#   """My_1"""
#     for spam_word in spam_words:
#         if spam_word.lower() in text.lower():
#             if space_around is False:
#                 return True
#             elif space_around is True:
#                 for word in text.split(' '):
#                     word = word.strip('., ,,')
#                     if word == spam_word:
#                         return True
#                     else:
#                         continue
#
#     return False


##################################################################################################

import re


def is_spam_words(text, spam_words, space_around=False):
    """GPT_chat"""
    text = text.lower()

    for spam_word in spam_words:
        if space_around:
            pattern = r'(^|\s)' + re.escape(spam_word) + r'($|\s|\.\,)'
            if re.search(pattern, text):
                return True
        else:
            if spam_word in text:
                return True

    return False

##################################################################################################


print(is_spam_words("Молох Передбачити третій параметр ", ["лох", "функції_"]))
print(is_spam_words("Молох Передбачити третій параметр", ["лох", "функції_"], True))

print(is_spam_words("Ты лох. Передбачити третій параметр  ", ["лох", "функції_"]))
print(is_spam_words("Ты лох, Передбачити третій параметр  ", ["лох", "функції_"], True))
