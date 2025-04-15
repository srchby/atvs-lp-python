import json

tasks = []

def save_tasks():
    with open("tasks.json", "w") as outfile:
        json.dump(tasks, outfile, indent=4)
        
def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as infile:
            tasks = json.load(infile)
    except FileNotFoundError:
        tasks = []
    
def get_task_date(task):
    day, month, year = map(int, task[1].split('/'))
    return (year, month, day)

def sorted_tasks(task_list):
    return sorted(task_list, key=get_task_date)

def add_task():
    name = input("Nome da tarefa: \n>> ")
    date = input("Prazo da tarefa (dd/mm/yy): \n>> ")
    day, month, year = map(int, date.split('/'))
    tasks.append([name, date, False])   

def mark_task():
    index = input(f"Escolher tarefa \n>> ")
    try:
        index = int(index)
        if 0 <= index < len(tasks):
            tasks[index][2] = True
        else:
            print("\nTarefa inválida\n")
    except ValueError:
        print(f"\nValor não válido\n")

load_tasks()

while True:
    tasks = sorted_tasks(tasks)
    print(f"Tarefas: ")
    for i, task in enumerate(tasks):
        print(f"\n{i}. \nNome: {task[0]} \nPrazo: {task[1]} \nCompleto: {task[2]}\n")
    
    save_tasks()
    
    action = int(input(f"1. Adicionar tarefa \n2. Completar tarefa \n3. Sair \n>> "))
    if (action == 1):
        add_task()
    elif (action == 2):
        mark_task()
    elif (action == 3):
        save_tasks()
        break
        