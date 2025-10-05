from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Página inicial."

@app.route("/produtos")
def produtos():
    return "Lista de produtos."

@app.route("/contato")
def contato():
    return "Página de contato."

if __name__ == "__main__":
    app.run(debug=True)