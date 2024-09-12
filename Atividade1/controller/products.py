from flask import Blueprint, request, redirect # type: ignore

criar_bp_produto = Blueprint('goproduct', __name__, template_folder='templates')
criar_bp_produto2 = Blueprint('goproduct2', __name__, template_folder='templates')
catalogo = [
        {
            "Produto": "Camiseta Primordial Oversized",
            "Preço": "R$ 127,99",
            "Imagem": "https://down-br.img.susercontent.com/file/sg-11134201-7qve2-lfgw2e8e6lz9e6",
            "id": 1
        },
        {
            "Produto": "Camiseta Ultra armor",
            "Preço": "R$ 147,99",
            "Imagem": "https://i.ebayimg.com/images/g/wV8AAOSwMMNkdkzB/s-l1200.webp",
            "id": 2
        },
        {
            "Produto": "Moletom Espadachim negro",
            "Preço": "R$ 227,99",
            "Imagem": "https://down-br.img.susercontent.com/file/66c8219e9159ac61a01f472c006d567b",
            "id": 3
        },
        {
            "Produto": "Camiseta Revenge Oversized",
            "Preço": "R$ 157,99",
            "Imagem": "https://www.indieapes.in/cdn/shop/files/1710852624_3480458_copy_2.jpg?v=1721852862",
            "id": 4
        },
        {
            "Produto": "Camiseta Era de ouro",
            "Preço": "R$ 87,99",
            "Imagem": "https://dcdn.mitiendanube.com/stores/003/023/206/products/berserk1-960865ef48ebb06ebb16852354765416-1024-1024.png",
            "id": 5
        },
        {
            "Produto": "Camiseta Sangue frio Oversized",
            "Preço": "R$ 127,99",
            "Imagem": "https://wolf1.in/cdn/shop/files/D468C807-D9B5-4934-B95B-12DC230519BA.png?v=1705048955&width=416",
            "id": 6
        },
    ]

dest = [
        {
            "Produto": "Camiseta Berserk Tales",
            "Preço": "R$ 137,90",
            "Imagem": "static/CamisaDesta1.jpg",
            "id": 7
        },
        {
            "Produto": "Moletom Eclipse",
            "Preço": "R$ 189,90",
            "Imagem": "static/CamisaDesta2.jpg",
            "id": 8
        },
        {
            "Produto": "Camiseta Oversized Sacrifice",
            "Preço": "R$ 119,90",
            "Imagem": "static/CamisaDesta3.jpg",
            "id": 9
        },
        {
            "Produto": "Camiseta Dragon Slayer",
            "Preço": "R$ 130,90",
            "Imagem": "static/CamisaDesta4.jpg",
            "id": 10
        },
        {
            "Produto": "Camiseta Tr4sh Berserk",
            "Preço": "R$ 119,90",
            "Imagem": "static/CamisaDesta5.jpg",
            "id": 11
        },
        {
            "Produto": "Camiseta Lovers Sacrifice",
            "Preço": "R$ 119,90",
            "Imagem": "static/CamisaDesta6.jpg",
            "id": 12
        },
        {
            "Produto": "Conjunto Caska Berserk",
            "Preço": "R$ 359,90",
            "Imagem": "static/CamisaDesta7.jpg",
            "id": 13
        }
    ]
estrelaimg = {'Imagem': 'https://img.icons8.com/fluency/48/star--v1.png'}

valorprod = []
valorprod2 = []

@criar_bp_produto.route('/goproduct', methods=['POST'])
def achar_prod():
    valor = int(request.form.get("numberid"))
    for item in catalogo:
        if valor == item['id']:
            valorprod.append({
                'Imagem': item["Imagem"],
                'Produto': item["Produto"],
                'Preço': item["Preço"]
            })
            return redirect('/product1')
    return redirect('/')

@criar_bp_produto2.route('/goproduct2', methods=['POST'])
def achar_prod2():
    valor2 = int(request.form.get("numberid2"))
    for item2 in dest:
        if valor2 == item2['id']:
            valorprod2.append({
                'Imagem': item2["Imagem"],
                'Produto': item2["Produto"],
                'Preço': item2["Preço"]
            })
            return redirect('/product2')
    return redirect('/')