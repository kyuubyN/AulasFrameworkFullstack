from flask import Blueprint, request, redirect # type: ignore

criar_bp = Blueprint('criar', __name__, template_folder='templates')
lista = []

class Aval:
    def __init__(self, nome, msg, star):
        self.nome = nome
        self.msg = msg
        self.star = star

@criar_bp.route("/criar", methods=['POST', ])
def criar():
    nome = request.form['nome']
    msg = request.form['feedback']
    star = request.form['estrelas']
    starint = int(star)
    aval = Aval(nome, msg, starint)
    lista.append(aval)
    return redirect('/')