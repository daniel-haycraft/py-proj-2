from flask import Flask, request, render_template, url_for, redirect
from abc import ABC, abstractmethod
import csv
from pprint import pprint
from cupcakes import get_cupcakes, add_to_order_csv, find_cupcake, read_price

app = Flask(__name__)

@app.route('/add-cupcakes/<name>')
def add_cupcake(name):
    cupcake = find_cupcake("cupcake.csv", name)
    print(cupcake)
    if cupcake:
        add_to_order_csv("orders.csv", cupcake=cupcake)
        return redirect(url_for('order'))
    else:
        return "sorry cupcake doesn't exist"
@app.route('/add-cater/<name>')
def add_cater(name):
    cupcake = find_cupcake("cupcake.csv", name)
    print(cupcake)
    if cupcake:
        add_to_order_csv("orders.csv", cupcake=cupcake)
        return redirect(url_for('order'))
    else:
        return "sorry cupcake doesn't exist"
@app.route('/one')
def one():
    return render_template('one.html', cupcakes = get_cupcakes('catering.csv'))

@app.route('/')
def all():
    return render_template('all.html', cupcakes = get_cupcakes('cupcake.csv'))
@app.route('/orders')
def order():
    return render_template('orders.html', cupcakes =  get_cupcakes('orders.csv'), total_price = read_price('orders.csv'))

# @app.route("/guide/<name>", methods=["DELETE"])
# def guide_delete(name):
#     slice(name)
#     return render_template('orders.html', cupcakes =  get_cupcakes('orders.csv'))
# need to do more research on subject matter i have to go to  work 


if __name__ == '__main__':
    app.run(debug = True, port = 8000, host = "localhost")