from abc import ABC, abstractmethod
import csv
from pprint import pprint

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

class Regular(Cupcake):
    size = "regular"

class Behemoth(Cupcake):
    size = "behemoth"

class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, flavor, icing, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.icing = icing
        self.sprinkles = []

mini_coffee_cupcake = Mini(" Pequeña magdalena de café", " Coffee", " Vanilla ", 5)
mini_coffee_cupcake.add_sprinkles("coffee")


behe = Behemoth(" Basic B", " Vanilla", " Chocolate ", None, 12)
regular = Regular(" The Not So Basic B", " Marble", " Birthday Cake", " Strawberry ", 8)
regular.add_sprinkles("House Mixture", "hi", "hello")
behe.add_sprinkles("Multicolored")
cupcake_list = [
    mini_coffee_cupcake,
    behe,
    regular
]


def open_read_file(filename):
    with open(filename) as file:
        reader = csv.DictReader(file)
        for words in reader:
            pprint(words)

def write_csv(file, cupcakes):
    with open(file, "w", newline='\n') as csvfile:
        fieldnames = ["size","name", "flavor", "icing", "filling", "price", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcakes, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price, "filling": cupcake.filling, "sprinkles": cupcake})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price,"filling": None, "sprinkles": cupcake.sprinkles})

write_csv("sample.csv", cupcake_list)

def append_csv(file, new_cupcakes):
    with open(file, "a", newline='\n') as csvfile:
        fieldnames = ["size","name", "flavor", "icing", "filling", "price", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for cupcake in new_cupcakes:
            
            if hasattr(mini_coffee_cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price,"sprinkles": cupcake.sprinkles})
append_csv("sample.csv", cupcake_list)


