from flask import Flask, render_template, request, redirect  # type: ignore

lista = []
app = Flask(__name__)

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


@app.route("/")
def index():
    return render_template(
        "index.html", catal=catalogo, avaliacoes=lista, desta=dest,
    estrela=estrelaimg)


@app.route("/feedback")
def feedback():
    return render_template("feedback.html")


class Aval:
    def __init__(self, nome, msg, star):
        self.nome = nome
        self.msg = msg
        self.star = star

@app.route("/criar", methods=['POST', ])
def criar():
    nome = request.form['nome']
    msg = request.form['feedback']
    star = request.form['estrelas']
    starint = int(star)
    aval = Aval(nome, msg, starint)
    lista.append(aval)
    return redirect('/')

app.run(debug=True)
