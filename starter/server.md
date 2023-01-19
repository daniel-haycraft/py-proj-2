from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template ("index.html")

@app.route('/information')
def info():
    return "<h1>Puppies are very cute</h1>"

@app.route('/information/<name>')
def yo_name(name):
    return f"<h1>getting information on {name.upper()}</h1>"


# @app.route('/puppy_latin/<names>')
# def puppy_lat(names):
#         if names [-1] == "y":
#             x = names.replace('y','iful')
#             return f"<h1>{x.upper()}</h1>"
#         else:
#             return f"<h1>{names.upper() + ('Y')}</h1>"


if __name__ == '__main__':
    app.debug = "development"
    app.run(debug = True, port = 8000, host = "localhost")