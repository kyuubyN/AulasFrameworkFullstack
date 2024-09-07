from flask import Flask, render_template, redirect, flash # type: ignore
from controller.bp import lista, criar_bp
from controller.cadastro import criar_bp_cad
from controller.login import criar_bp_login, session, contas

app = Flask(__name__)

app.secret_key = 'test'

app.register_blueprint(criar_bp_cad)

app.register_blueprint(criar_bp)

app.register_blueprint(criar_bp_login)

estrelaimg = {'Imagem': 'https://img.icons8.com/fluency/48/star--v1.png'}

catalogo = [
        {
            "Produto": "Camiseta Primordial Oversized",
            "Preço": "R$ 127,99",
            "Imagem": "https://down-br.img.susercontent.com/file/sg-11134201-7qve2-lfgw2e8e6lz9e6",
        },
        {
            "Produto": "Camiseta Ultra armor",
            "Preço": "R$ 147,99",
            "Imagem": "https://i.ebayimg.com/images/g/wV8AAOSwMMNkdkzB/s-l1200.webp",
        },
        {
            "Produto": "Moletom Espadachim negro",
            "Preço": "R$ 227,99",
            "Imagem": "https://down-br.img.susercontent.com/file/66c8219e9159ac61a01f472c006d567b",
        },
        {
            "Produto": "Camiseta Revenge Oversized",
            "Preço": "R$ 157,99",
            "Imagem": "https://www.indieapes.in/cdn/shop/files/1710852624_3480458_copy_2.jpg?v=1721852862",
        },
        {
            "Produto": "Camiseta Era de ouro",
            "Preço": "R$ 87,99",
            "Imagem": "https://dcdn.mitiendanube.com/stores/003/023/206/products/berserk1-960865ef48ebb06ebb16852354765416-1024-1024.png",
        },
        {
            "Produto": "Camiseta Sangue frio Oversized",
            "Preço": "R$ 127,99",
            "Imagem": "https://wolf1.in/cdn/shop/files/D468C807-D9B5-4934-B95B-12DC230519BA.png?v=1705048955&width=416",
        },
    ]


dest = [
        {
            "Produto": "Camiseta Berserk Tales",
            "Preço": "R$ 137,90",
            "Imagem": "static/CamisaDesta1.jpg",
        },
        {
            "Produto": "Moletom Eclipse",
            "Preço": "R$ 189,90",
            "Imagem": "static/CamisaDesta2.jpg",
        },
        {
            "Produto": "Camiseta Oversized Sacrifice",
            "Preço": "R$ 119,90",
            "Imagem": "static/CamisaDesta3.jpg",
        },
        {
            "Produto": "Camiseta Dragon Slayer",
            "Preço": "R$ 130,90",
            "Imagem": "static/CamisaDesta4.jpg",
        },
        {
            "Produto": "Camiseta Tr4sh Berserk",
            "Preço": "R$ 119,90",
            "Imagem": "static/CamisaDesta5.jpg",
        },
        {
            "Produto": "Camiseta Lovers Sacrifice",
            "Preço": "R$ 119,90",
            "Imagem": "static/CamisaDesta6.jpg",
        },
        {
            "Produto": "Conjunto Caska Berserk",
            "Preço": "R$ 359,90",
            "Imagem": "static/CamisaDesta7.jpg",
        }
    ]

titleindex = "Berserk Store - Inicio"
@app.route("/")
def index():
    return render_template(
        "index.html", catal=catalogo, avaliacoes=lista, desta=dest,
    estrela=estrelaimg, title=titleindex)


@app.route("/feedback")
def feedback():
    return render_template("feedback.html", title=titleindex)

@app.route("/base")
def base():
    return render_template("base.html", title=titleindex)

@app.route("/login")
def login():
    return render_template("signin.html", title=titleindex)

@app.route("/cadastro")
def cad():
    return render_template("signup.html", title=titleindex)

@app.route("/cadastroerror")
def caderror():
    return render_template("signuperror.html", title=titleindex)

@app.route("/sucesso")
def success():
    return render_template("sucesso.html", title=titleindex)

@app.route('/perfil')
def profile():
    if 'user' in session:
        email = session['user']  
        
        perfil_usuario = next((u for u in contas if u['email'] == email), None)
        if perfil_usuario:
            return render_template('profile.html', perfil=perfil_usuario)
        else:
            flash('Usuário não encontrado', 'error')
            return redirect('/login')
    else:
        flash('Você precisa fazer login', 'error')
        return redirect('/login')


app.run(debug=True)
