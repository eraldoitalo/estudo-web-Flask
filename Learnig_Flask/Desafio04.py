#Desafio de Código – Conceito 4 (GET e POST)
#Crie uma aplicação Flask com:
#Uma rota /formulario que aceite GET e POST.
#Se for GET, deve exibir a mensagem: "Preencha o formulário".
#Se for POST, deve exibir a mensagem: "Dados recebidos com sucesso!".

from flask import Flask, request

app = Flask(__name__)

@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "GET":
        return "Preencha o formulário"
    elif request.method == "POST":
        return "Dados recebidos com sucesso!"
    
if __name__ == "__main__":
    app.run(debug=True)