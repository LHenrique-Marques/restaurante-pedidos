
class Cardapio:
    def __init__(self):
        self.itens = []
        self.precos = list()


    def adicionar_item(self, item, preco):
        self.itens.append(item)
        self.precos.append(preco)

    def print_itens(self):
        print("\n"*30)
        print("="*50)
        print("Cardápio:")
        for i in range(len(self.itens)):
            print(f" {i + 1} {str(self.itens[i]).ljust(45,'.')}...{self.precos[i]}")
        
        item_escolhido = int(input(f"Escolher opção [1- {len(self.itens)}]:  ")) - 1       
        return self.itens[item_escolhido] , self.precos[item_escolhido]
        


def popular_itens(cardapio, l_itens, l_precos):
    for i in range(len(l_itens)):
        cardapio.adicionar_item(l_itens[i], l_precos[i])


class Pedido:
    def __init__(self):
        self.item = None
        self.quantidade = 0
        self.valor_item = 0

    def escolher_pedido(self,cardapio):
        item, preco = cardapio.print_itens()
        print(f"{item}: {preco}")
        qt_itens = int(input("Quantos você quer : "))
        total = float(preco) * int(qt_itens)
        print(f"""
        ----------------------------------------------------------
        ({qt_itens}) {item} : R${preco}
        Total : R${total}
        ----------------------------------------------------------
        
        """)
        confirmado = input("Confirma s/n:  ").upper()
        if confirmado == "S":
            self.item = item
            self.precos = preco
            self.quantidade = qt_itens