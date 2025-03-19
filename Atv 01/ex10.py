def primeCheck(a):
    for n in range(2, int(a ** 0.5) + 1):
        if a % n == 0:
            return False
    return True

while (True):
    num = int(input("Envie um número inteiro maior que 1: "))
    result = primeCheck(num)
    if (result):
        print(f"{num} é primo")
        break
    else:
        print(f"{num} não é primo")
        break