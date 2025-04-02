def student_avg(a,b,c):
    avg = (a+b+c) / 3
    return avg

while True:
    print("Coloque 3 notas:")
    a = int(input(">> "))
    b = int(input(">> "))
    c = int(input(">> "))
    avg = student_avg(a,b,c)
    if (avg < 7):
        print(f"Média: {avg} \nReprovado")
    else:
        print(f"Média: {avg} \nAprovado")