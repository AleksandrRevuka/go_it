from collections import defaultdict, deque


words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']

words = deque(words)
words.append('last')
words.appendleft('first')
words.insert(1, 'middle')
print(words)     

print(words.pop()) 
print(words.popleft())  
print(list(words)) 



# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(grouped_words)