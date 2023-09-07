from classes import *
from informacoes import *

# criar uma função que transforme as duas variáveis em listas,
# e utilize o método adicionar_item para inseri-los no cardápio.

cardapio = Cardapio()
popular_itens(cardapio, aux_itens.split(";\n") , aux_precos.split())


# Instanciar um produto
# Escolher um item do cardapio para este pedido
# Printar os dados do pedido

pedido = Pedido()

#escolher um item do menu
#pedido.escolher_item(cardapio)
#print(pedido.item , pedido. quantidade, pedido.valor_pedido)

pedido.escolher_pedido(cardapio)

