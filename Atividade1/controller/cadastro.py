from flask import Blueprint, request, redirect, flash # type: ignore

criar_bp_cad = Blueprint('cadastrar', __name__, template_folder='templates')

dados_cadastro = []
@criar_bp_cad.route("/cadastrar", methods=['POST'])
def cadastro():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    for usuario in dados_cadastro:
        if usuario['email'] == email:
            flash('Email já cadastrado, tente outro.', 'error')
            return redirect('/cadastroerror')
    dados = {
        'nome': nome,
        'email': email,
        'senha': senha
    }
    dados_cadastro.append(dados)
    flash('Cadastro realizado com sucesso!', 'success')
    return redirect('/sucesso')