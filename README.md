# Sistema de Atendimento em Loja
* Aluno: Lucas Morais de Moura
* Curso: Bacharelado Interdisciplinar em Ciências e Tecnologia.
* Disciplina: Fundamentos de Computação
* Professor: Rondineli Seba

##  Descrição

Este programa simula um sistema simples de atendimento em uma loja, permitindo que o usuário escolha produtos, informe a quantidade e visualize o valor total da compra.

O sistema foi desenvolvido utilizando conceitos fundamentais da linguagem Python.

---

##  Lógica do Programa

O programa inicia solicitando o nome do usuário.

Em seguida, é exibido um menu interativo com opções de produtos disponíveis.

O usuário pode:

* Escolher um produto
* Informar a quantidade desejada
* Realizar várias operações até decidir sair

O sistema possui dados internos, como:

* Nome dos produtos
* Preços

Durante a execução, o programa:

1. Valida as entradas do usuário (evita valores inválidos)
2. Associa o produto ao seu respectivo preço (usando `match-case`, simulando switch)
3. Calcula o valor total da compra
4. Aplica desconto de 10% caso o valor seja maior que R$100
5. Exibe o resumo da compra
6. Permite repetir o processo (menu interativo)

---

##  Funcionalidades

* Entrada de dados pelo usuário
* Processamento de informações
* Saída de resultados
* Uso de variáveis:

  * `int` (quantidade, opção)
  * `str` (nome, produto)
  * `float` (preço, total)
  * `bool` (desconto)
* Estruturas condicionais:

  * `if/else`
  * `match-case` (switch)
* Validação de entrada (tratamento de erros)
* Menu interativo (repetição com `while`)

---

##  Como executar

1. Instale o Python
2. Abra o terminal na pasta do projeto
3. Execute o comando:

```bash
python Appy.py
```

---

##  Exemplo de uso

```
Digite seu nome: Lucas

=== MENU DE PRODUTOS ===
1 - Camisa (50.0)
2 - Calça (100.0)
3 - Tênis (200.0)
0 - Sair

Escolha o produto: 1
Quantidade: 3

=== RESUMO ===
Cliente: Lucas
Produto: Camisa
Quantidade: 3
Desconto aplicado: 10%
Total: 135.0
```

---

##  Observações

O programa utiliza a estrutura `match-case` para simular um switch na escolha do produto, e `if/else` para aplicar condições como o desconto.

Também foi implementada validação de entrada para garantir que o usuário informe dados corretos, além de um menu interativo que permite múltiplas operações.
