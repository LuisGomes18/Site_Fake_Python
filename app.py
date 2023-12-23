from os import urandom
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.secret_key = urandom(16)

@app.route('/')
def index():
    """
    A function that serves as the route handler for the '/' endpoint.

    Returns:
        The rendered 'index.html' template.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
