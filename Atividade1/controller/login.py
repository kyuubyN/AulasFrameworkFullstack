from flask import Blueprint, request, redirect, session # type: ignore
from controller.cadastro import dados_cadastro
contas = dados_cadastro

criar_bp_login = Blueprint('logar', __name__, template_folder='templates')
@criar_bp_login.route("/logar", methods=['POST'])
def get_dados():
    email_log = request.form.get("email_login")
    senha_log = request.form.get("senha_login")
    
    for data in contas:
        if email_log == data["email"] and senha_log == data["senha"]:
            session['user'] = email_log
            print('Login bem-sucedido!', 'success')
            return redirect('/perfil')
        else:
            print('Email ou senha incorretos. Tente novamente.', 'error')
    
    return redirect('/login')
