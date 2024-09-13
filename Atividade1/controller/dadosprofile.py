from flask import Blueprint, redirect, request

pegar_dados = Blueprint("pegar_dados", __name__, template_folder="templates")

endereco = []

@pegar_dados.route("/endereco", methods=["POST"])
def data():
    if len(endereco) > 0 and "id" in endereco[0]:
        del endereco[0]
        print("PAMONHA")
    else: 
        pass
    cep = request.form.get("cep")
    bairro = request.form.get("bairro")
    rua = request.form.get("rua")
    cidade = request.form.get("cidade")
    estado = request.form.get("uf")
    numero = request.form.get("number")
    database = {
        "cep": cep,
        "bairro": bairro,
        "rua": rua,
        "cidade": cidade,
        "estado": estado,
        "numero": numero,
        "id": "id"
    }
    endereco.append(database)
    return redirect("/perfil")