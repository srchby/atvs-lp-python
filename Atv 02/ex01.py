tasks = [["clean", "13 april", False],["exercise","14 april", True]]
while True:
    print(f"Tarefas: ")
    for i, task in enumerate(tasks):
        print(f"{i}. \nNome: {task[0]} \nPrazo: {task[1]} \nCompleto: {task[2]}")
    action = int(input(f"1. Adicionar tarefa \n2. Completar tarefa \n>> "))
    if (action == 1):
        name = input("Nome da tarefa: \n>> ")
        date = input("Prazo da tarefa: \n>> ")
        tasks.append([name, date, False])   
    elif (action == 2):
        index = input(f"Escolher tarefa \n>> ")
        try:
            index = int(index)
            if 0 <= index < len(tasks):
                tasks[index][2] = True
            else:
                print("Tarefa inválida")
        except ValueError:
            print(f"Valor não válido")