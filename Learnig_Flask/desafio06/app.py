from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'chave-secreta' # necessário para usar session e flash 

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/enviar', methods=['POST'])
def enviar():
    nome = request.form.get('nome', '').strip()
    email = request.form.get('email', '').strip()
    idade = request.form.get('idade', '').strip()
    # validação simples
    if not nome or not email or not idade:
        flash('X todos os campos são obrigatórios!', 'error')
        session['nome']= nome
        session['email']= email
        session['idade']= idade
        return redirect(url_for('index'))

    if not idade.isdigit() or int (idade)<=0:
        flash('X idade deve ser um numero positivo!', 'error')
        return redirect(url_for('index'))
    
    # passou na validação 
    flash('✓ dados enviados com sucesso!', 'success')
    return redirect(url_for('resultado', nome=nome, email=email, idade=idade))

@app.route('/resultado')
def resultado():
    nome = request.args.get('nome')
    email = request.args.get('email')
    idade = request.args.get('idade')
    return render_template('resultado.html', nome=nome, email=email, idade=idade)

if __name__ == '__main__':
    app.run(debug=True)
