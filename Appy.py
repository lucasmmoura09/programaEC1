print("=== LOJA ===")

nome = input("Digite seu nome: ")

print("1 - Camisa (50)")
print("2 - Calça (100)")
print("3 - Tênis (200)")

opcao = int(input("Escolha: "))
quantidade = int(input("Quantidade: "))

# escolha do produto (switch)
match opcao:
    case 1:
        produto = "Camisa"
        preco = 50
    case 2:
        produto = "Calça"
        preco = 100
    case 3:
        produto = "Tênis"
        preco = 200
    case _:
        print("Opção inválida")
        exit()

total = preco * quantidade

# condição
if total > 100:
    total = total * 0.9
    desconto = True
else:
    desconto = False

print("\nResumo:")
print(nome, produto, quantidade)

if desconto:
    print("Teve desconto")

print("Total:", total)