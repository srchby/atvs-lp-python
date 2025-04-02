def sum(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    return a / b

while True:
    print("Insira dois números:")
    a = int(input(">> "))
    b = int(input(">> "))
    print(f"Soma dos números: {sum(a,b)}")
    print(f"Subtração dos números: {sub(a,b)}")
    print(f"Multiplicação dos números: {mult(a,b)}")
    print(f"Divsão dos números: {div(a,b)}")