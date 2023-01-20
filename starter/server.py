from flask import Flask, request, render_template, url_for, redirect
from abc import ABC, abstractmethod
import csv
from pprint import pprint
from cupcakes import get_cupcakes, add_to_order_csv, find_cupcake

app = Flask(__name__)

@app.route('/add-cupcakes/<name>')
def add_cupcake(name):
    cupcake = find_cupcake("cupcake.csv", name)
    print(cupcake)
    if cupcake:
        add_to_order_csv("orders.csv", cupcake=cupcake)
        return redirect(url_for('home'))
    else:
        return "sorry cupcake doesn't exist"

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/one')
def one():
    return render_template('one.html')
@app.route('/all')
def all():
    return render_template('all.html', cupcakes = get_cupcakes('cupcake.csv'))
@app.route('/orders')
def order():
    return render_template('orders.html')



# @app.route('/puppy_latin/<names>')
# def puppy_lat(names):
#         if names [-1] == "y":
#             x = names.replace('y','iful')
#             return f"<h1>{x.upper()}</h1>"
#         else:
#             return f"<h1>{names.upper() + ('Y')}</h1>"


if __name__ == '__main__':
    app.run(debug = True, port = 8000, host = "localhost")