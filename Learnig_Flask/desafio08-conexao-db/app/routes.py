from flask import Blueprint, render_template, request, redirect, url_for
from .models import User
from . import db

main = Blueprint("main", __name__)

@main.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

@main.route("/novo", methods=["GET", "POST"])
def novo_usuario():
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")

        novo = User(nome=nome, email=email)
        db.session.add(novo)
        db.session.commit()

        return redirect(url_for("main.index"))
    
    return render_template("form.html")