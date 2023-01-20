from abc import ABC, abstractmethod
import csv
from pprint import pprint
from flask import Flask, render_template




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

class Dozen(Cupcake):
    size = "12-Regular"

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
baker_dozen = Dozen(" Gluten Free", " Marble", " Vanilla", None, 8)
baker_dozen.add_sprinkles('Chocolate', 'Strawberry')
#  name, flavor, icing, filling, price
behe = Behemoth(" Basic B", " Vanilla", " Chocolate ", None, 12)
regular = Regular(" The Not So Basic B", " Marble", " Birthday Cake", " Strawberry ", 8)
regular.add_sprinkles("House Mixture", "hi", "hello")
behe.add_sprinkles("Multicolored")

cupcake_list = [
    mini_coffee_cupcake,
    behe,
    regular,
    baker_dozen
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

write_csv("cupcake.csv", cupcake_list)

def append_csv(file, new_cupcakes):
    with open(file, "a", newline='\n') as csvfile:
        fieldnames = ["size","name", "flavor", "icing", "filling", "price", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for cupcake in new_cupcakes:
            
            if hasattr(new_cupcakes, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price,"sprinkles": cupcake.sprinkles})
append_csv("cupcake.csv", cupcake_list)

my_first_order= [mini_coffee_cupcake]

def add_to_order_csv(file, order):
    with open(file, "a", newline='\n') as csvfile:
        fieldnames = ["size","name", "flavor", "icing", "filling", "price", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for cupcake in order:
            
            if hasattr(order, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price,"sprinkles": cupcake.sprinkles})
def find_cupcake(file,name):
    for cupcake in get_cupcakes(file):
        if cupcake['name'] == name:
            return cupcake

def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader




add_to_order_csv('order.csv', my_first_order)





    # run { source venv/bin/activate }