from flask import Blueprint, request, redirect  # type: ignore

criar_bp = Blueprint("criar", __name__, template_folder="templates")

lista = []


@criar_bp.route("/criar", methods=["POST"])
def criar():
    nome = request.form["nome"]
    msg = request.form["feedback"]
    star = int(request.form["estrelas"])
    aval = {"nome": nome, "msg": msg, "star": star}
    lista.append(aval)
    return redirect("/")
