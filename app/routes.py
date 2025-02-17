from main import app
from flask import render_template

# rotas
@app.route("/")
def homepage():
    dados = {"profissao": "Idol", "skzoo": "Dwaekki"}
    nome = "Changbin"
    return render_template('index.html', nome=nome, dados=dados)

@app.route("/contato")
def contato():
    return render_template('contato.html')
