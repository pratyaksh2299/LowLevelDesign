from abc import ABC, abstractmethod

class Coffee(ABC):

    @abstractmethod
    def make(self):
        pass


# base component
class SimpleCoffee(Coffee):

    def make(self):
        return 'making simple coffee'


# decorator interface
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee


# concrete decorator
class CoffeeWithMilk(CoffeeDecorator):
    def make(self):
        return f'{self.coffee.make()} with milk'


# concrete decorator
class CoffeeWithSugar(CoffeeDecorator):
    def make(self):
        return f'{self.coffee.make()} with sugar'


# concrete decorator
class CoffeeWithoutMilk(CoffeeDecorator):
    def make(self):
        return f'{self.coffee.make()} without milk'
        

if __name__ == '__main__':

    coffee: Coffee = SimpleCoffee()
    print(coffee.make())

    milk_coffee: Coffee = CoffeeWithMilk(SimpleCoffee())
    print(milk_coffee.make())

    milk_sugar_coffee: Coffee = CoffeeWithSugar(CoffeeWithMilk(SimpleCoffee()))
    print(milk_sugar_coffee.make())
