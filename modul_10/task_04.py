class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, new_color):
        Animal.color = new_color
    
first_animal = Animal('Bob', 43)
second_animal = Animal('Sara', 32)
first_animal.change_color("red")
first_animal.color = "red"
