from flask import request, redirect, Blueprint

alterarIcon = Blueprint("icon", __name__, template_folder="templates")
imgMain = {
    "Imagem": "../static/iconProfile.jpg"
}
caminho = "../static/"
@alterarIcon.route("/icon", methods=["POST"])
def alterar():
    img = request.form.get("arquivo")
    if img.find(".jpg") != -1 or img.find(".png") != -1 or img.find("jpeg") != -1:
        imgMain["Imagem"] = caminho + img
        return redirect('/perfil')
    else:
        print("Arquivo não compativel")
        return redirect('/perfil')
