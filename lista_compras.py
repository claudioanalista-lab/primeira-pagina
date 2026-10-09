#Resolução em Python (lista_compras.py):

def mostrar_lista(lista):
    print("\n--- LISTA DE COMPRAS ---")
    if not lista:
        print("A lista está vazia.")
    else:
        for i, item in enumerate(lista):
            print(f"{i} - {item}")

def cadastrar_item(lista):
    novo_item = input("\nDigite o nome do novo item: ").strip()
    if novo_item:
        lista.append(novo_item)
        print(f"'{novo_item}' foi adicionado à lista!")
    else:
        print("Nome de item inválido.")
        

def excluir_item(lista):
    mostrar_lista(lista)
    if not lista:
        return
    try:
        indice = int(input("\nDigite o número (índice) do item que deseja excluir: "))
        if 0 <= indice < len(lista):
            removido = lista.pop(indice)
            print(f"'{removido}' foi removido da lista!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def modificar_item(lista):
    mostrar_lista(lista)
    if not lista:
        return
    try:
        indice = int(input("\nDigite o número (índice) do item que deseja modificar: "))
        if 0 <= indice < len(lista):
            novo_nome = input(f"Digite o novo nome para '{lista[indice]}': ").strip()
            if novo_nome:
                antigo = lista[indice]
                lista[indice] = novo_nome
                print(f"'{antigo}' foi alterado para '{novo_nome}'!")
            else:
                print("Nome inválido.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def main():
    lista_compras = ["arroz", "feijão", "pão", "leite", "café", "açúcar", "óleo"]
    
    while True:
        print("\n=== MENU - LISTA DE COMPRAS ===")
        print("1 - Mostra lista")
        print("2 - Cadastrar item na lista")
        print("3 - Excluir item da lista")
        print("4 - Modificar item da lista")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            mostrar_lista(lista_compras)
        elif opcao == "2":
            cadastrar_item(lista_compras)
        elif opcao == "3":
            excluir_item(lista_compras)
        elif opcao == "4":
            modificar_item(lista_compras)
        elif opcao == "0":
            print("Saindo do programa... Até mais!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
