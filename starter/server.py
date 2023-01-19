from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> Hello Puppy</h1>"

@app.route('/information')
def info():
    return "<h1>Puppies are very cute</h1>"

@app.route('/information/<name>')
def yo_name(name):
    return f"<h1>getting information on {name.upper()}</h1>"


if __name__ == '__main__':
    app.debug = "development"
    app.run(debug = True, port = 8000, host = "localhost")