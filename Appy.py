print("=== SISTEMA DE LOJA ===")

nome = input("Digite seu nome: ")

while True:

    print("\n=== MENU DE PRODUTOS ===")
    print("1 - Camisa (50.0)")
    print("2 - Calça (100.0)")
    print("3 - Tênis (200.0)")
    print("0 - Sair")

    try:
        opcao = int(input("Escolha o produto: "))
    except:
        print("Digite apenas números!")
        continue

    if opcao == 0:
        print("Encerrando sistema...")
        break

    if opcao not in [1, 2, 3]:
        print("Opção inválida!")
        continue

    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("Quantidade inválida!")
            continue
    except:
        print("Digite um número válido!")
        continue

    produto = ""
    preco = 0.0
    desconto = False

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

    total = preco * quantidade

    if total > 100:
        total = total * 0.9
        desconto = True
    else:
        desconto = False

    print("\n=== RESUMO ===")
    print("Cliente:", nome)
    print("Produto:", produto)
    print("Quantidade:", quantidade)

    if desconto:
        print("Desconto aplicado: 10%")

    print("Total:", total)
