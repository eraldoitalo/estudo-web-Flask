from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form['nome']
    email = request.form['email']
    idade = request.form['idade']
    # redireciona passando os dados via query string
    return redirect(url_for('resultado', nome=nome, email=email, idade=idade))

@app.route('/resultado')
def resultado():
    nome = request.args.get('nome')
    email = request.args.get('email')
    idade = request.args.get('idade')
    return render_template('resultado.html', nome=nome, email=email, idade=idade)

if __name__ == '__main__':
    app.run(debug=True)
