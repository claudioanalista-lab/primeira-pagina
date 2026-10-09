#  - lista_compras_simples.py

lista = ["arroz", "feijão", "pão", "leite", "café", "açúcar", "óleo"]

opcao = ""

while opcao != "0":
    print("\n=== MENU - LISTA DE COMPRAS ===")
    print("1 - Mostrar lista")
    print("2 - Adicionar item")
    print("3 - Remover item")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- LISTA DE COMPRAS ---")
        if len(lista) == 0:
            print("A lista está vazia.")
        else:
            for item in lista:
                print("-", item)

    elif opcao == "2":
        novo_item = input("\nDigite o nome do novo item: ")
        lista.append(novo_item)
        print(f"'{novo_item}' foi adicionado à lista!")

    elif opcao == "3":
        item_remover = input("\nDigite o nome do item para remover: ")
        if item_remover in lista:
            lista.remove(item_remover)
            print(f"'{item_remover}' foi removido da lista!")
        else:
            print("Item não encontrado!")

    elif opcao == "0":
        print("Saindo do programa... Até mais!")

    else:
        print("Opção inválida! Tente novamente.")
