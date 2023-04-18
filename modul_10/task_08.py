class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"
    

class CatDog(Cat, Dog):
    def info(self):
        return f"{self.nickname}-{self.weight}"
    

class DogCat(Dog, Cat):
    def info(self):
        return f"{self.nickname}-{self.weight}"
    

cat_d = CatDog("Sherlock", 24)
    
dog_c = DogCat("Simon", 10)


print(cat_d.say(), cat_d.info())
print(dog_c.say(), dog_c.info())