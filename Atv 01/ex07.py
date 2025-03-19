def lastSqr(odd):
    pred = odd - 1
    lastOdd = odd + 2
    return (pred * pred) - lastOdd

while (True):
    odd = int(input("Insira número impar: "))
    print(f"A diferença entre o quadrado do número anterior e do próximo número ímpar é {lastSqr(odd)}")
    break