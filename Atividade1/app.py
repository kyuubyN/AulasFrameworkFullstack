from flask import Flask, render_template # type: ignore

app = Flask(__name__)

catalogo = [
    {
        'Produto': 'Camiseta Primordial Oversized',
        'Preço': 'R$ 127,99',
        'Imagem': 'https://down-br.img.susercontent.com/file/sg-11134201-7qve2-lfgw2e8e6lz9e6'
    },
    {
        'Produto': 'Camiseta Ultra armor',
        'Preço': 'R$ 147,99',
        'Imagem': 'https://i.ebayimg.com/images/g/wV8AAOSwMMNkdkzB/s-l1200.webp'
    },
    {
        'Produto': 'Moletom Espadachim negro',
        'Preço': 'R$ 227,99',
        'Imagem': 'https://down-br.img.susercontent.com/file/66c8219e9159ac61a01f472c006d567b'
    },
    {
        'Produto': 'Camiseta Revenge Oversized',
        'Preço': 'R$ 157,99',
        'Imagem': 'https://www.indieapes.in/cdn/shop/files/1710852624_3480458_copy_2.jpg?v=1721852862'
    },
    {
        'Produto': 'Camiseta Era de ouro',
        'Preço': 'R$ 87,99',
        'Imagem': 'https://dcdn.mitiendanube.com/stores/003/023/206/products/berserk1-960865ef48ebb06ebb16852354765416-1024-1024.png'
    },
    {
        'Produto': 'Camiseta Sangue frio Oversized',
        'Preço': 'R$ 127,99',
        'Imagem': 'https://wolf1.in/cdn/shop/files/D468C807-D9B5-4934-B95B-12DC230519BA.png?v=1705048955&width=416'
    }
]
@app.route('/')
def index():
    return render_template('index.html', catal=catalogo)

app.run()