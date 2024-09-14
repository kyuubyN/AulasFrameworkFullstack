from flask import Flask, render_template, redirect, flash # type: ignore
from controller.bp import lista, criar_bp
from controller.cadastro import criar_bp_cad
from controller.login import criar_bp_login, session, contas
from controller.iconprofile import alterarIcon, imgMain
from controller.products import catalogo, dest, estrelaimg, criar_bp_produto, criar_bp_produto2, valorprod, valorprod2
from controller.dadosprofile import pegar_dados, endereco
app = Flask(__name__)

app.secret_key = 'teste'

app.register_blueprint(criar_bp_cad)

app.register_blueprint(criar_bp)

app.register_blueprint(criar_bp_login)

app.register_blueprint(criar_bp_produto)

app.register_blueprint(criar_bp_produto2)

app.register_blueprint(alterarIcon)

app.register_blueprint(pegar_dados)

titleindex = "Berserk Store"
class Routes():
    
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
                return render_template('profile.html', perfil=perfil_usuario, title=titleindex, icon=imgMain, data=endereco)
            else:
                flash('Usuário não encontrado', 'error')
                return redirect('/login')
        else:
            flash('Você precisa fazer login', 'error')
            return redirect('/login')


    @app.route('/error')
    def error():
        return render_template('404.html', title=titleindex)
    
    @app.route('/product1')
    def product1():
        if valorprod:
            return render_template('products.html', valpd=valorprod[-1], title=titleindex)
        return redirect('/') 

    @app.route('/product2')
    def product2():
        if valorprod2:
            return render_template('products2.html', valpd=valorprod2[-1], title=titleindex)
        return redirect('/')
