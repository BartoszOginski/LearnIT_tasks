from flask import Flask, render_template

app = Flask(__name__)


# Zadanie 1
@app.route("/me")
def me():
    return "Jan Kowalski"


# Zadanie 2
@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    suma = num1 + num2
    return f"Wynik to: {suma}"


# Zadanie 3 i 4
@app.route("/movies")
def movies():
    filmy = [
        "Interstellar",
        "Incepcja",
        "Gladiator"
    ]

    page_title = "Moje ulubione filmy"

    return render_template(
        "movies.html",
        movies=filmy,
        page_title=page_title
    )


if __name__ == "__main__":
    app.run(debug=True)