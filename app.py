from flask import Flask, render_template, request, url_for, redirect, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sklep.db"
db = SQLAlchemy(app)

# Baza danych w słownikach / liście słowników (według sekcji 5.3 i 6.3 z obu lekcji)
class Produkt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nazwa = db.Column(db.String(100), nullable=False)
    cena = db.Column(db.Float, nullable=False)
    dostepny = db.Column(db.Boolean, default=True)
    data_dodania = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f"<Produkt {self.nazwa}>"
with app.app_context():
    db.create_all()


# ==========================================
# TRASY Z LEKCJI 05
# ==========================================

# Zadanie 1: Powitanie
@app.route("/czesc/<imie>")
def czesc(imie):
    return f"Cześć, {imie}!"

@app.route("/czesc/<imie>/<int:wiek>")
def czesc_wiek(imie, wiek):
    return f"Cześć, {imie}, masz {wiek} lat"


# Zadanie 2: Kalkulator
@app.route("/dodaj/<int:a>/<int:b>")
def dodaj_kalkulator(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/odejmij/<int:a>/<int:b>")
def odejmij(a, b):
    return f"{a} - {b} = {a - b}"

@app.route("/pomnoz/<int:a>/<int:b>")
def pomnoz(a, b):
    return f"{a} * {b} = {a * b}"

@app.route("/podziel/<int:a>/<int:b>")
def podziel(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a / b}"

@app.route("/potega/<int:a>/<int:b>")
def potega(a, b):
    return f"{a} ^ {b} = {a ** b}"


# Zadanie 3: Tabliczka mnożenia
@app.route("/tabliczka/<int:n>")
def tabliczka(n):
    if n < 1 or n > 20:
        return "Liczba spoza przedziału 1-20", 400
    wynik = ""
    for i in range(1, 11):
        wynik += f"{n} * {i} = {n * i}<br>"
    return wynik


# Zadanie 6 (Lekcja 05): Przekierowanie
@app.route("/start")
def start():
    return redirect(url_for("index"))


# ==========================================
# TRASY Z LEKCJI 06
# ==========================================

# Zadanie 1: Pierwszy szablon
@app.route("/")
def index():
    return render_template("index.html", projekt="Sklep 4TP", imie="Oskar Biurkowski")


# Zadanie 2 & Zadanie 5: Lista i Pusta lista
@app.route("/lista")
def lista():
    return render_template("lista.html", produkty=PRODUKTY)


# Zadanie 3: Szczegóły
@app.route("/element/<int:id>")
def produkt(id):
    p_znaleziony = None
    for p in PRODUKTY:
        if p["id"] == id:
            p_znaleziony = p
            break
    if not p_znaleziony:
        abort(404)
    return render_template("szczegoly.html", p=p_znaleziony)


# Zadanie 6: Szukaj (GET)
@app.route("/szukaj")
def szukaj():
    q = request.args.get("q", "")
    wyniki = [p for p in PRODUKTY if q.lower() in p["nazwa"].lower()] if q else []
    return render_template("szukaj.html", q=q, wyniki=wyniki)


# Zadanie 7: Dodaj (POST)
@app.route("/dodaj", methods=["GET", "POST"])
def dodaj():
    if request.method == "POST":
        nowy = {
            "id": len(PRODUKTY) + 1,
            "nazwa": request.form["nazwa"],
            "cena": float(request.form["cena"]),
            "kategoria": request.form.get("kategoria", "Ogólne"),
            "dostepny": True if request.form.get("dostepny") else False
        }
        PRODUKTY.append(nowy)
        return redirect(url_for("lista"))
    return render_template("dodaj.html")


if __name__ == "__main__":
    app.run(debug=True)