def celsToFahr(cels):
    fahr = (cels * 1.8) + 32
    return fahr

while (True):
    cels = float(input("Insira temperatura em Celsius: "))
    print(f"A temperatura em Fahrenheit é: {celsToFahr(cels)}")
    break