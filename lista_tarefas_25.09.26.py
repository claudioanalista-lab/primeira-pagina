# LISTA DE TAREFAS #

# 1 - Mostrar todas as TAREFAS
# 2 - Mostrar tarefas concluidas
# 3 - Mostrar tarefas nao concluidas
# 4 - Mostrar tarefas por prioridade
# 5 - Cadastrar tarefa nova
# 6 - Finalizar tarefa
# 7 - Remover tarefas
# 0 - Sair
  
  # tarefas = [
  #   {"Titulo":"Estudar","Concluida":"Sim","Prioridade":"Alta"}
  #   {"Titulo":"Ler","Concluida":"Nao","Prioridade":"Baixa"}
    
  # ]
  
  # mostrar as tarefas concluidas ou nao de um dos jeitos abaixo:
  # [x] Estudar | Alta
  # [ ] Ler     | Baixa
  
tarefas = [
    {"Titulo": "Estudar", "Concluida": "Sim", "Prioridade": "Alta"},
    {"Titulo": "Ler", "Concluida": "Nao", "Prioridade": "Baixa"},
    {"Titulo": "Exercitar", "Concluida": "Nao", "Prioridade": "Alta"}
]

opcao = ""

while opcao != "0":
    print("\n=== MENU - LISTA DE TAREFAS ===")
    print("1 - Mostrar todas as TAREFAS")
    print("2 - Mostrar tarefas concluidas")
    print("3 - Mostrar tarefas nao concluidas")
    print("4 - Mostrar tarefas por prioridade")
    print("5 - Cadastrar tarefa nova")
    print("6 - Finalizar tarefa")
    print("7 - Remover tarefas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("\n--- TODAS AS TAREFAS ---")
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada.")
        else:
            for t in tarefas:
                status = "[x]" if t["Concluida"] == "Sim" else "[ ]"
                print(f"{status} {t['Titulo']} | {t['Prioridade']}")

    elif opcao == "2":
        print("\n--- TAREFAS CONCLUÍDAS ---")
        encontrada = False
        for t in tarefas:
            if t["Concluida"] == "Sim":
                print(f"[x] {t['Titulo']} | {t['Prioridade']}")
                encontrada = True
        if not encontrada:
            print("Nenhuma tarefa concluída encontrada.")

    elif opcao == "3":
        print("\n--- TAREFAS NÃO CONCLUÍDAS ---")
        encontrada = False
        for t in tarefas:
            if t["Concluida"] == "Nao":
                print(f"[ ] {t['Titulo']} | {t['Prioridade']}")
                encontrada = True
        if not encontrada:
            print("Nenhuma tarefa pendente encontrada.")

    elif opcao == "4":
        p_busca = input("Digite a prioridade desejada (Alta, Media, Baixa): ").strip().capitalize()
        print(f"\n--- TAREFAS COM PRIORIDADE {p_busca.upper()} ---")
        encontrada = False
        for t in tarefas:
            if t["Prioridade"].capitalize() == p_busca:
                status = "[x]" if t["Concluida"] == "Sim" else "[ ]"
                print(f"{status} {t['Titulo']} | {t['Prioridade']}")
                encontrada = True
        if not encontrada:
            print("Nenhuma tarefa encontrada com essa prioridade.")

    elif opcao == "5":
        print("\n--- CADASTRAR NOVA TAREFA ---")
        titulo = input("Digite o título da tarefa: ").strip()
        prioridade = input("Digite a prioridade (Alta, Media, Baixa): ").strip().capitalize()
        nova_tarefa = {
            "Titulo": titulo,
            "Concluida": "Nao",
            "Prioridade": prioridade
        }
        tarefas.append(nova_tarefa)
        print(f"Tarefa '{titulo}' cadastrada com sucesso!")

    elif opcao == "6":
        print("\n--- FINALIZAR TAREFA ---")
        titulo_finalizar = input("Digite o título da tarefa a finalizar: ").strip()
        encontrada = False
        for t in tarefas:
            if t["Titulo"].lower() == titulo_finalizar.lower():
                t["Concluida"] = "Sim"
                print(f"Tarefa '{t['Titulo']}' marcada como concluída!")
                encontrada = True
                break
        if not encontrada:
            print("Tarefa não encontrada.")

    elif opcao == "7":
        print("\n--- REMOVER TAREFA ---")
        titulo_remover = input("Digite o título da tarefa a remover: ").strip()
        encontrada = False
        for t in tarefas:
            if t["Titulo"].lower() == titulo_remover.lower():
                tarefas.remove(t)
                print(f"Tarefa '{t['Titulo']}' removida com sucesso!")
                encontrada = True
                break
        if not encontrada:
            print("Tarefa não encontrada.")

    elif opcao == "0":
        print("Saindo da Lista de Tarefas... Até mais!")

    else:
        print("Opção inválida! Tente novamente.")
