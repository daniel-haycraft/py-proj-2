from abc import ABC, abstractmethod
import csv
from pprint import pprint
from flask import Flask, render_template, url_for, redirect




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
    size = "Regular"
    def __init__(self, name, flavor, icing, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.icing = icing
        self.sprinkles = []
two_dozen = Dozen('Munchies', 'Vanilla', 'Chocolate', 20)
class CrazyCakes(Cupcake):
    size = "Small Cakes"
    def __init__(self, name, flavor, icing, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.icing = icing
        self.sprinkles = []
three_dozen = CrazyCakes('Small Party', 'Vanilla', 'Chocolate', 35)

class Large_Cakes(Cupcake):
    size =  "12inches in diameter"
    def __init__(self, name, flavor, icing, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.icing = icing
        self.sprinkles = []
    
dozen =  Large_Cakes('Wedding', 'Marble', 'Marble', 20)

two_dozen.add_sprinkles("Vanilla")
big_orders = [
    dozen,
    two_dozen,
    three_dozen
]

class Mini(Cupcake):
    size = "mini"
    def __init__(self, name, flavor, icing, price):
        self.name = name
        self.flavor = flavor
        self.price = price
        self.icing = icing
        self.sprinkles = []

mini_coffee_cupcake = Mini("Pequeña magdalena de café", " Coffee", " Vanilla ", 5)
mini_coffee_cupcake.add_sprinkles("coffee")
baker_dozen = Dozen("Gluten Free", "Marble", "Vanilla", 8)
baker_dozen.add_sprinkles('Chocolate', 'Strawberry')
#  name, flavor, icing, filling, price
behe = Behemoth("Basic B", "Vanilla", " Chocolate ", "No Filling options", 12)
regular = Regular("The Not So Basic B", "Marble", "Birthday Cake", "Strawberry ", 8)
regular.add_sprinkles("House Mixture")
behe.add_sprinkles("Multicolored")

regular.add_sprinkles('Vanilla')

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
            return words


def write_csv(file, cupcakes):
    with open(file, "w", newline='\n') as csvfile:
        fieldnames = ["size","name", "flavor", "icing", "price", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for cupcake in cupcakes:
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price, "filling": cupcake.filling, "sprinkles": cupcake})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price, "sprinkles": cupcake.sprinkles})


def append_csv(file, new_cupcakes):
    with open(file, "a", newline='\n') as csvfile:
        fieldnames = ["size","name", "flavor", "icing", "price", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for cupcake in new_cupcakes:
            
            if hasattr(cupcake, "filling"):
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price, "filling": cupcake.filling, "sprinkles": cupcake.sprinkles})
            else:
                writer.writerow({"size": cupcake.size, "name": cupcake.name, "flavor": cupcake.flavor, "icing":cupcake.icing, "price": cupcake.price,"sprinkles": cupcake.sprinkles})

my_first_order= [mini_coffee_cupcake]


def get_cupcakes(file):
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        return reader

def find_cupcake(file, names):
    for cupcake in get_cupcakes(file):
        print(cupcake)
        if cupcake["name"] == names:
            return cupcake
    return None

def add_to_order_csv(file, cupcake):
    with open(file, "a", newline='\n') as csvfile:
        fieldnames = ["size","name", "flavor", "icing", "price", "filling", "sprinkles"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow(cupcake)

def read_price(file):
    x=[]
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        for words in reader:
            x.append(words['price'])
        return list(map(int,x))

# converted_numbers = read_price('orders.csv')
# print(converted_numbers)






    # run { source venv/bin/activate }