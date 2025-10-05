from flask import Flask

# Criar a aplicação Flask
app = Flask(__name__)

# Definir rota principal
@app.route("/")
def home():
    return "Flask é um micro framework para criação de paginas web em python."

# Rota de comparção
@app.route("/comparacao")
def comparacao():
    return "Djando já vem com mais recurços prontos"

@app.route("/pagina")
def pagina():
    return "Essa seria a home da minha página"

# Executar servidor
if __name__ == "__main__":
    app.run(debug=True)