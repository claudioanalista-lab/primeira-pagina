tarefas = [
    {"Titulo": "Estudar", "Concluida": "Sim", "Prioridade": "Alta"},
    {"Titulo": "Ler", "Concluida": "Nao", "Prioridade": "Baixa"},
    {"Titulo": "Exercitar", "Concluida": "Nao", "Prioridade": "Alta"}
]

while True:
    print("\n--- LISTA DE TAREFAS ---")
    print("1 - Mostrar todas as TAREFAS")
    print("2 - Mostrar tarefas concluidas")
    print("3 - Mostrar tarefas nao concluidas")
    print("4 - Mostrar tarefas por prioridade")
    print("5 - Cadastrar tarefa nova")
    print("6 - Finalizar tarefa")
    print("7 - Remover tarefas")
    print("0 - Sair")
    
    opcao = input("Escolha uma opcao: ")
    
    if opcao == "0":
        break
    elif opcao == "1":
        for t in tarefas:
            status = "[x]" if t["Concluida"] == "Sim" else "[ ]"
            print(f"{status} {t['Titulo']} | {t['Prioridade']}")
    elif opcao == "2":
        for t in tarefas:
            if t["Concluida"] == "Sim":
                print(f"[x] {t['Titulo']} | {t['Prioridade']}")
    elif opcao == "3":
        for t in tarefas:
            if t["Concluida"] == "Nao":
                print(f"[ ] {t['Titulo']} | {t['Prioridade']}")
    elif opcao == "4":
        prio = input("Qual prioridade (Alta/Baixa)? ")
        for t in tarefas:
            if t["Prioridade"].lower() == prio.lower():
                status = "[x]" if t["Concluida"] == "Sim" else "[ ]"
                print(f"{status} {t['Titulo']} | {t['Prioridade']}")
    elif opcao == "5":
        titulo = input("Titulo da tarefa: ")
        prio = input("Prioridade (Alta/Baixa): ")
        tarefas.append({"Titulo": titulo, "Concluida": "Nao", "Prioridade": prio})
    elif opcao == "6":
        titulo = input("Titulo da tarefa a finalizar: ")
        for t in tarefas:
            if t["Titulo"].lower() == titulo.lower():
                t["Concluida"] = "Sim"
    elif opcao == "7":
        titulo = input("Titulo da tarefa a remover: ")
        tarefas = [t for t in tarefas if t["Titulo"].lower() != titulo.lower()]


# 