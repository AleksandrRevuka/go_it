class Point:
    def __init__(self, x, y) -> None:
        self.__x = None
        self.__y = None
        self.cor_x = x
        self.cor_y = y

    @property
    def cor_x(self):
        return self.__x
    
    @cor_x.setter
    def cor_x(self, new_x):
        self.__x = new_x

    @property
    def cor_y(self):
        return self.__y
    
    @cor_y.setter
    def cor_y(self, new_y):
        self.__y = new_y


cor = Point(5, 10)
cor.cor_x = 9
print(cor.cor_x)