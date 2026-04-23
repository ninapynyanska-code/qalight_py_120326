

class Car:

    def __new__(cls, *args, **kwargs):
        print(f"__new__ викликаний для {cls.__name__}")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, make, model):
        print(f"__init__ викликаний")
        self.make = make
        self.model = model

# blank_car = Car()  # __new__ викликаний а на ініті фейл

print("**")

my_car = Car("Toyota", "Camry")

"""
`__new__()` має повернути екземпляр класу. Це обов'язковий метод для створення об'єкта.
`__init__()` - це метод-конструктор, який викликається **ДРУГИЙ** і відповідає за ініціалізацію атрибутів об'єкта.
"""

class CarParams:

    def __init__(self, make, model):
        self.make = make
        self.__model = model
        print(f"Машина {make} {model} створена")

    def __del__(self):
        print(f"Машина {self.make} {self.__model} знищена")
    
    # def __repr__(self):
    #     return f"CarParams('{self.make}', '{self.__model}')"
    
    def __str__(self):
        return f"The {self.make} {self.__model} object"
    
    def __len__(self):
        return 100



car = CarParams("Toyota", "Camry")
print(car)
print(len(car))
del car

class Person():
    def __init__(self, age:int = 0) -> None:
        self.__age = age
        self.__name = ""

    @property
    def age(self):
        return f"{self.__age} years old"
    
    @age.setter
    def age(self, years: int):
        if not isinstance(years, int):
            raise ValueError("add_year must be int")
        if years >= self.__age:
            self.__age = years
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name:str):
        if not isinstance(new_name, str):
            raise ValueError("new_name must be str")
        if len(new_name) >= len(self.__name):
            self.__name = new_name



bobby = Person(25)
print(bobby.age)
bobby.age = 24
print(bobby.age)
bobby.name = "bobby"
print(bobby.name)
bobby.name = "bob"
print(bobby.name)