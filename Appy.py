print("=== LOJA ===")

# entrada (str)
nome = input("Digite seu nome: ")

print("\n1 - Camisa (50.0)")
print("2 - Calça (100.0)")
print("3 - Tênis (200.0)")

# entrada (int)
opcao = int(input("Escolha o produto: "))
quantidade = int(input("Quantidade: "))

# variáveis
produto = ""
preco = 0.0   # float
desconto = False  # bool

# ----------------------------
# SWITCH (match-case)
# ----------------------------
match opcao:
    case 1:
        produto = "Camisa"
        preco = 50.0
    case 2:
        produto = "Calça"
        preco = 100.0
    case 3:
        produto = "Tênis"
        preco = 200.0
    case _:
        print("Opção inválida")
        exit()

# processamento
total = preco * quantidade

# ----------------------------
# IF / ELSE (condição)
# ----------------------------
if total > 100:
    total = total * 0.9
    desconto = True
else:
    desconto = False

# saída
print("\n=== RESUMO ===")
print("Cliente:", nome)
print("Produto:", produto)
print("Quantidade:", quantidade)

if desconto:
    print("Desconto aplicado: 10%")

print("Total:", total)
