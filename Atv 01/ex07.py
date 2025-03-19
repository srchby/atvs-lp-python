def lastSqr(odd):
    pred = odd - 1
    nextOdd = odd + 2
    return (pred ** 2) - nextOdd

while (True):
    odd = int(input("Insira número impar: "))
    print(f"A diferença entre o quadrado do número anterior e do próximo número ímpar é {lastSqr(odd)}")
    break