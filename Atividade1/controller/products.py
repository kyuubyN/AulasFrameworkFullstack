from flask import Blueprint, request, redirect  # type: ignore

criar_bp_produto = Blueprint("goproduct", __name__, template_folder="templates")
criar_bp_produto2 = Blueprint("goproduct2", __name__, template_folder="templates")
catalogo = [
    {
        "Produto": "Camiseta Primordial Oversized",
        "Preço": "R$ 127,99",
        "Imagem": "https://down-br.img.susercontent.com/file/sg-11134201-7qve2-lfgw2e8e6lz9e6",
        "id": 1,
        "cor":"Preto"
    },
    {
        "Produto": "Camiseta Ultra armor",
        "Preço": "R$ 147,99",
        "Imagem": "https://i.ebayimg.com/images/g/wV8AAOSwMMNkdkzB/s-l1200.webp",
        "id": 2,
        "cor":"Preto"
    },
    {
        "Produto": "Moletom Espadachim negro",
        "Preço": "R$ 227,99",
        "Imagem": "https://down-br.img.susercontent.com/file/66c8219e9159ac61a01f472c006d567b",
        "id": 3,
        "cor":"Preto"
    },
    {
        "Produto": "Camiseta Revenge Oversized",
        "Preço": "R$ 157,99",
        "Imagem": "https://cdn.dooca.store/292/products/sg18-camiseta-berserk-aberta.jpg?v=1585144656&webp=0",
        "id": 4,
        "cor":"Preto"
    },
    {
        "Produto": "Camiseta Era de ouro",
        "Preço": "R$ 87,99",
        "Imagem": "https://dcdn.mitiendanube.com/stores/003/023/206/products/berserk1-960865ef48ebb06ebb16852354765416-1024-1024.png",
        "id": 5,
        "cor":"Branco"
    },
    {
        "Produto": "Camiseta Sangue frio Oversized",
        "Preço": "R$ 127,99",
        "Imagem": "https://wolf1.in/cdn/shop/files/D468C807-D9B5-4934-B95B-12DC230519BA.png?v=1705048955&width=416",
        "id": 6,
        "cor":"Preto"
    },
]

dest = [
    {
        "Produto": "Camiseta Berserk Tales",
        "Preço": "R$ 137,90",
        "Imagem": "static/CamisaDesta1.jpg",
        "id": 7,
        "cor":"Preto"
    },
    {
        "Produto": "Moletom Eclipse",
        "Preço": "R$ 189,90",
        "Imagem": "https://down-br.img.susercontent.com/file/db7f66b579b15c02286202c0d042d358",
        "id": 8,
        "cor":"Preto"
    },
    {
        "Produto": "Camiseta Oversized Sacrifice",
        "Preço": "R$ 119,90",
        "Imagem": "static/CamisaDesta3.jpg",
        "id": 9,
        "cor":"Preto"
    },
    {
        "Produto": "Camiseta Dragon Slayer",
        "Preço": "R$ 130,90",
        "Imagem": "static/CamisaDesta4.jpg",
        "id": 10,
        "cor":"Preto"
    },
    {
        "Produto": "Camiseta Tr4sh Berserk",
        "Preço": "R$ 119,90",
        "Imagem": "static/CamisaDesta5.jpg",
        "id": 11,
        "cor":"Preto"
    },
    {
        "Produto": "Camiseta Lovers Sacrifice",
        "Preço": "R$ 119,90",
        "Imagem": "static/CamisaDesta6.jpg",
        "id": 12,
        "cor":"Cinza"
    },
    {
        "Produto": "Conjunto Caska Berserk",
        "Preço": "R$ 359,90",
        "Imagem": "static/CamisaDesta7.jpg",
        "id": 13,
        "cor":"Branco"
    },
]
estrelaimg = {"Imagem": "https://img.icons8.com/fluency/48/star--v1.png"}

valorprod = []
valorprod2 = []


@criar_bp_produto.route("/goproduct", methods=["POST"])
def achar_prod():
    valor = int(request.form.get("numberid"))
    for item in catalogo:
        if valor == item["id"]:
            valorprod.append(
                {
                    "Imagem": item["Imagem"],
                    "Produto": item["Produto"],
                    "Preço": item["Preço"],
                    "Cor": item["cor"]
                }
            )
            return redirect("/product1")
    return redirect("/")


@criar_bp_produto2.route("/goproduct2", methods=["POST"])
def achar_prod2():
    valor2 = int(request.form.get("numberid2"))
    for item2 in dest:
        if valor2 == item2["id"]:
            valorprod2.append(
                {
                    "Imagem": item2["Imagem"],
                    "Produto": item2["Produto"],
                    "Preço": item2["Preço"],
                    "Cor": item2["cor"]
                }
            )
            return redirect("/product2")
    return redirect("/")
