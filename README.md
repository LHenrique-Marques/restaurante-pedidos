# Sistema de Compra para Restaurantes
> Status do Projeto: Em progresso.
```
Programa 100% em python usando Orientação de Objetos.
```
<h2> Orientações do Projeto </h2>


<h3>Você deverá desenvolver uma aplicação para um evento que controle o consumo de bebidas por pessoa.
Para isto você deverá armazenar em uma lista (lista_convidados) os dados relevantes dos convidados as classes abaixo:</h3>

- [ ]Convidado


> nome : str <br>
> telefone : str <br>
> cartao _de_consumo : Cartao <br>
> finalizar_consumo() <br>
> realizar_pedido() <br>

<h3>Você também deverá criar uma lista com 100 cartões.</h3>


- [ ]Cartao

> numero : int <br>
> itens_consumo : lista de Pedidos <br>
> ativo : bool. True=Ativo. False=Inativo <br>
> ativar_cartao() <br>
> desativar_cartao() <br>
> adicionar_pedido() <br>

- [ ]Pedido

> item : str <br>
> quantidade : int <br>
> valor_pedido : float <br>
> escolher_item() <br>

<h3>Você deverá ter um cardápio com itens e bebidas.</h3>

- [x]Cardapio

> itens : list() <br>
> precos : list() <br>
> adicionar_itens() <br>
> retirar_itens() <br>


