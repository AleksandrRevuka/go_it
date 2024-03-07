from abc import ABC, abstractmethod


class ComputerFactory(ABC):

    @abstractmethod
    def make_laptop(self):
        pass

    @abstractmethod
    def make_desktop(self):
        pass


class HomeComputerFactory(ComputerFactory):

    def make_laptop(self):
        return HomeLaptop()
    
    def make_desktop(self):
        return HomeDesktop()
    

class CorporateComputerFactory(ComputerFactory):

    def make_laptop(self):
        return CorporateLaptop()
    
    def make_desktop(self):
        return CorporateDesktop()
    

class Laptop(ABC):
    def specs(self):
        pass


class Desktop(ABC):
    def specs(self):
        pass


class HomeLaptop(Laptop):
    def specs(self):
        print("Home Laptop: Lower performance, larger screen")


class HomeDesktop(Desktop):
    def specs(self):
        print("Home Desktop: Moderate performance, affordable")


class CorporateLaptop(Laptop):
    def specs(self):
        print("Corporate Laptop: High performance, security features")


class CorporateDesktop(Desktop):
    def specs(self):
        print("Corporate Dasktop: High performance, manageability")


def client(factory):
    laptop = factory.make_laptop()
    desktop = factory.make_desktop()

    print("Laptop Specs:")
    laptop.specs()

    print("\nDesktop Specs:")
    desktop.specs()


def main():
    print("Home Computers:")
    client(HomeComputerFactory())

    print("\nCorporate Computers:")
    client(CorporateComputerFactory())

if __name__ == "__main__":
    main()