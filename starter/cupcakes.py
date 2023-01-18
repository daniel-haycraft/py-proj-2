from abc import ABC, abstractmethod
import csv


class Cupcake:
    size = "regular"
    def __init__(self, name, flavor, icing, filling, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.icing = icing
        self.filling = filling
        self.sprinkles = []

    def add_sprinkles(self, *args):
        for sprink in args:
            self.sprinkles.append(sprink)

    
    @abstractmethod 
    def calculate_price(self,quantity):
        return quantity * self.price

class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, flavor, icing, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.icing = icing
        self.sprinkles = []

mini_coffee_cupcake = Mini ("pequeña magdalena de café","Coffee", "Vanilla", 5)
mini_coffee_cupcake.add_sprinkles("coffee")
mini_coffee_cupcake.calculate_price(5)

with open("sample.csv") as cupcakes:
    reader = csv.DictReader(cupcakes)