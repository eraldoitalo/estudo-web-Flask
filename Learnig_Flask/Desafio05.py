#Desafio de Código – Conceito 5 (Formulários HTML e POST)
#Crie uma pequena aplicação Flask que:
#Exiba um formulário HTML na rota /cadastro com campos:
#nome
#e-mail
#Quando o formulário for enviado (método POST), mostre na tela:
    #"Bem-vindo, [nome]! Seu e-mail é [email]."

from flask import Flask, request

app = Flask(__name__)

@app.route("/cadastro", methods=["GET"])
def cadastro_form():
    return '''
        <form method="POST" action="/cadastro">
            Nome: <input type="text" name="nome"><br>
            E-mail: <input type="email" name="email"><br>
            <input type="submit" value="Cadastrar">
        </form>
    '''

@app.route("/cadastro", methods=["POST"])
def cadastro_submit():
    nome = request.form.get("nome")
    email = request.form.get("email")
    return f"Bem-vindo, {nome}! Seu e-mail é {email}."

if __name__ == "__main__":
    app.run(debug=True)
