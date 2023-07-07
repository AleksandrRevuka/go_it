class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y
        
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if isinstance(value, bool):
            self.__x = None
        elif isinstance(value, (int, float)):
            self.__x = value
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        if isinstance(value, bool):
            self.__y = None
        elif isinstance(value, (int, float)):
            self.__y = value
