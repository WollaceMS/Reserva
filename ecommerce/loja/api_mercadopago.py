import mercadopago


import os
from dotenv import load_dotenv

load_dotenv()

public_key = os.getenv("public_key")
token = os.getenv("token")


def criar_pagamento(itens_pedido, link):
    sdk = mercadopago.SDK(token)

    # itens que estão sendo comprados no formato de dict
    itens = []
    for item in itens_pedido:
        quantidade = int(item.quantidade)
        nome = item.item_estoque.produto.nome
        preco_unitario = float(item.item_estoque.produto.preco)
        itens.append({
            'title': nome,
            'quantity': quantidade,
            'unit_price': preco_unitario,  
        })

    # valor total
    preference_data = {
        'items': itens,
        'back_urls': {
            'success': link,
            'pending': link,
            'failure': link,
            }

    }
    resposta = sdk.preference().create(preference_data)
    link_pagamento = resposta['response']['init_point']
    id_pagamento = resposta['response']['id']
    return link_pagamento, id_pagamento
