# Flask Hello World
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World from Flask!'

@app.route('/about')
def about():
    return 'This is a Flask learning app.'

if __name__ == '__main__':
    app.run(debug=True)
