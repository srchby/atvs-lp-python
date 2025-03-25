def classAvg(classes, students):
    avg = students / classes
    stuByCl = []
    distStu = 0
    for i in range(classes):
        remainingStu = students - distStu
        remainingCl = classes - i
        stuInCl = round(avg * (i + 1)) - round(avg * i)
        stuByCl.append(stuInCl)
        distStu += stuInCl
        
    return stuByCl

while True:
    schClass = int(input("Envie a quantidade de salas: "))
    schStudents = int(input("Envie a quantidade total de alunos: "))
    schAvg = classAvg(schClass, schStudents)
    
    print(f"Alunos para {schClass} turmas: ")
    biggerThanForty = False;
    for i, stu in enumerate(schAvg, start=1):
        print(f"Turma {i}: {stu} Estudantes")
        if (stu > 40):
            biggerThanForty = True
            
    if (biggerThanForty):
        print("Há alguma sala com mais de 40 alunos")