class RegistryMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if not hasattr(cls, '_registry'):
            cls._registry = {}
        else:
            cls._registry[cls.__name__] = cls

class Plugin(metaclass=RegistryMeta):
    pass

class Plugin1(Plugin):
    pass

class Plugin2(Plugin):
    pass

# Виведемо всі класи, які були автоматично зареєстровані
print(Plugin._registry)
