from collections import UserString


class NumberString(UserString):
    def number_count(self):
        return len(list(filter(lambda x: x.isnumeric(), self.data)))
        # return len([x for x in self.data if x.isnumeric()])
    
numbers = NumberString('4f1grttu678')

print(numbers.number_count())


data = '4f1grttu678'
x = len(''.join(filter(lambda x: x.isdigit(), data)))
print(x) # 6