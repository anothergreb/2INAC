tarefas = []

while True:
    print ("\n- - - GERENCIADOR DE TAREFAS ---")
    print ("1. Adicionar Tarefa ")
    print ("2. Listar Tarefas ")
    print ("3. Sair ")
    opcao = int(input(" Escolha uma opcao : "))

    if opcao == 1:
        item = input("Digite a nova tarefa: ")
        tarefas.append(item)
        print("Tarefa adicionada!")
    elif opcao == 2:
        print ("\nSUA LISTA :")
        for i, t in enumerate(tarefas, 1):
            print(f"{i}, {t}")
    elif opcao == 3:
        print (" Encerrando o programa ...")
        break
    else:
        print(" Opcao invalida !")