def classAvg(classes, students):
    avg = students // classes
    return avg

while True:
    schClass = input("Envie a quantidade de salas: ")
    schStudents = input("Envie a quantidade total de alunos: ")
    schAvg = classAvg(schClass, schStudents)
    
    if (schAvg > 40):
        print("A média é mais de 40 alunos por sala!")
        break
    else:
        print(f"A média de alunos por classe é {schAvg}")
        break