# Sistema de Compra para Restaurantes
> Status do Projeto: Em progresso.
```
Programa 100% em python usando Orientação de Objetos.
```
<h3>Funções</h3>

- [x] Possui menu organizado com opções de esolhas.
- [x] Opção de Alterar o Cardapio.
- [x] Opção de Auto Popular o Cardapio com itens padrão.
- [x] Função de mostrar o cardápio.
- [x] Gerar um Pedido.
- [x] Possuí opção de adicionar vários itens no cardápio.

<h2> Orientações do Projeto </h2>


<h3>Você deverá desenvolver uma aplicação para um evento que controle o consumo de bebidas por pessoa.
Para isto você deverá armazenar em uma lista (lista_convidados) os dados relevantes dos convidados as classes abaixo:<h3>

- []<h4>Convidado</h4>


> nome : str
> telefone : str
> cartao _de_consumo : Cartao
> finalizar_consumo()
> realizar_pedido()

<h3>Você também deverá criar uma lista com 100 cartões.</h3>


- [] <h4> Cartao </h4>

> numero : int
> itens_consumo : lista de Pedidos
> ativo : bool. True=Ativo. False=Inativo
> ativar_cartao()
> desativar_cartao()
> adicionar_pedido()

- [] <h4> Pedido </h4>

> item : str
> quantidade : int
> valor_pedido : float
> escolher_item()

<h3>Você deverá ter um cardápio com itens e bebidas.</h3>

- [x] <h3> Cardapio </h3>

> itens : list()
> precos : list()
> adicionar_itens()
> retirar_itens()


