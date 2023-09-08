from classes import *
from informacoes import *
cardapio = Cardapio()
popular_itens(cardapio, aux_itens.split(";\n") , aux_precos.split())




pedido = Pedido()



pedido.escolher_pedido(cardapio)

