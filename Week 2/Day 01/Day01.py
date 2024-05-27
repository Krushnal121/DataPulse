class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

dog1 = Dog("Buddy", 3)
print(dog1.bark())  # Output: Buddy says woof!

class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

animals = [Cat(), Dog()]
for animal in animals:
    print(animal.speak())  # Output: Meow Woof

class Car:
    def __init__(self, model, year):
        self.__model = model  # Private attribute
        self.year = year

    def get_model(self):
        return self.__model

car1 = Car("Toyota", 2020)
print(car1.get_model())  # Output: Toyota
