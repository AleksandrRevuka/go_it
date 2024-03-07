from abc import ABC, abstractmethod


class CoffeeType:
    ESPRESSO = 1
    AMERICANO = 2
    CAFFE_LATTE = 3
    CAPPUCCINO = 4


class CoffeeShop(ABC):
    @abstractmethod
    def create_coffee(self, coffee_type):
        pass

    def order_coffee(self, coffee_type):
        coffee = self.create_coffee(coffee_type)
        coffee.make_coffee()
        coffee.pour_into_cup()
        print("Here's your coffee! Thank you, come again.")


class Coffee(ABC):
    @abstractmethod
    def make_coffee(self):
        pass

    @abstractmethod
    def pour_into_cup(self):
        pass

# Конкретні класи кави
class Americano(Coffee):
    def make_coffee(self):
        print("Making Americano")

    def pour_into_cup(self):
        print("Pouring Americano into cup")

class Cappuccino(Coffee):
    def make_coffee(self):
        print("Making Cappuccino")

    def pour_into_cup(self):
        print("Pouring Cappuccino into cup")

class CaffeLatte(Coffee):
    def make_coffee(self):
        print("Making Caffe Latte")

    def pour_into_cup(self):
        print("Pouring Caffe Latte into cup")

class Espresso(Coffee):
    def make_coffee(self):
        print("Making Espresso")

    def pour_into_cup(self):
        print("Pouring Espresso into cup")


# Кав'ярня в італійському стилі
class ItalianCoffeeShop(CoffeeShop):
    def create_coffee(self, coffee_type):
        if coffee_type == CoffeeType.ESPRESSO:
            return Espresso()
        elif coffee_type == CoffeeType.AMERICANO:
            return Americano()
        elif coffee_type == CoffeeType.CAFFE_LATTE:
            return CaffeLatte()
        elif coffee_type == CoffeeType.CAPPUCCINO:
            return Cappuccino()

# Кав'ярня в американському стилі
class AmericanCoffeeShop(CoffeeShop):
    def create_coffee(self, coffee_type):
        if coffee_type == CoffeeType.ESPRESSO:
            return Espresso()
        elif coffee_type == CoffeeType.AMERICANO:
            return Americano()
        elif coffee_type == CoffeeType.CAFFE_LATTE:
            return CaffeLatte()
        elif coffee_type == CoffeeType.CAPPUCCINO:
            return Cappuccino()

# Використання
def main():
    italian_coffee_shop = ItalianCoffeeShop()
    italian_coffee_shop.order_coffee(CoffeeType.CAPPUCCINO)

    american_coffee_shop = AmericanCoffeeShop()
    american_coffee_shop.order_coffee(CoffeeType.CAFFE_LATTE)

if __name__ == "__main__":
    main()