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
    
banco_de_img = [
    {
        "Icon": "https://preview.redd.it/more-brazilian-miku-v0-ganp0j85c9kd1.jpeg?width=640&crop=smart&auto=webp&s=ba13afa4a9957fb2df12119aebab2abd7ba57336",
    },
    {
        "Icon": "https://i.pinimg.com/736x/fa/15/3f/fa153fcc6502210c22103df750abfc85.jpg",
    },
    {
        "Icon": "https://i.pinimg.com/564x/5e/68/31/5e68315f992d9c118fec1e0c5e5e3dbb.jpg",
    },
    {
        "Icon": "https://i.pinimg.com/736x/3f/38/3a/3f383a1d3ac00ec284ff4bf1f9544764.jpg",
    },
    {
        "Icon": "https://i.pinimg.com/736x/b9/8d/67/b98d67bff773c527f0c390feaaf471e1.jpg",
    },
    {
        "Icon": "https://i.pinimg.com/736x/05/22/67/05226723f0881bf7bd1805e992fd975a.jpg"
    },
    {
        "Icon": "https://64.media.tumblr.com/9022962c0c79773557dbeb66111aaee7/dd9587a7dda0cc4b-35/s250x400/497d4dd26d04710eb5d1cd4006ae1345286a74ad.jpg",
    },
    {
        "Icon": "https://static.wikia.nocookie.net/berserk/images/b/be/Schierke_at_SpiritMansion_Doorstep.png/revision/latest/scale-to-width-down/654?cb=20170421183609",
    },
    
    
]
