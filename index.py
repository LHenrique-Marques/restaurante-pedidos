from classes import *
from informacoes import *
cardapio = Cardapio() #Atribui a classe Cardapio a variavel cardapio
pedido = Pedido() #Atribui a classe Pedido a variavel pedido
popular_itens(cardapio, aux_itens.split(";\n") , aux_precos.split()) #Popula o Cardapio automaticamente
cardapio.apenas_mostra() #Usa o metodo da classe cardapio para apenas mostrar os itens do cardapio
while True:
    try:
        #Inicia o menu fazendo com que o usuario escolha se quer realizar ou alternar um pedido
        inicio = int(input("""
            Menu de Inicialização...
            Digite a opção do que você deseja fazer.
            
            1 - Alterar o Cardápio
            2 - Realizar um pedido
        Escolha o número da sua opção: """))
            
        if inicio == 1:
            #faz com que se a escolha for Alternar o Cardapio mande para este menu de escolha remover ou adicionar item.
            escolha_1 = int(input("""
            O que você deseja fazer ?
            1 - Adicionar item.
            2 - Remover item.
            Escolha o número da sua opção: """))
            if escolha_1 == 1:  
                #faz com que se a escolha adicionar item for escolhida Adicione um item a lista                  
                try:
                    item_novo = input("Digite o nome do item: ")
                    preco_novo = float(input("Digite o preço do produto: "))
                    cardapio.adicionar_item(item_novo,preco_novo)
                    continue            
                    
                except:
                    input("Você fez algo de errado, tente novamente.")

            elif escolha_1 == 2:
                #Faz com que se a escolha for remover o item a pessoa escolha o indice do item escolhido para ser removido.
                try:
                    cardapio.remover_item(int(input("Digite o número do pedido que deseja remover:  ")) - 1)
                    continue
                except:
                    input("Você não escolheu um item valido...")

        elif inicio == 2:
            #faz com que o cliente escolha seu pedido.
            pedido.escolher_pedido(cardapio)
            
    except:
        input("Erro....Você não escolheu uma opção valida....")
                

cardapio.apenas_mostra()




