from flask import Flask

app = Flask(__name__)

@app.route("/usuario/<nome>")
def usuario(nome):
    return f"Olá, {nome}!"

@app.route("/quadrado/<int:num>")
def quadrado(num):
    return f"O quadrado de {num} é {num ** 2}"


if __name__ == "__main__":
    app.run(debug=True)
