def carRental(kilometers, days):
    if kilometers > 100:
        totalPrice = ((kilometers - 100) * 12) + (90 * days)
        return totalPrice
    else:
        totalPrice = 90 * days
        return totalPrice
    
kilometers = float(input("Insira quilomêtros andados: "))
days = int(input("E quantos dias em que o carro foi usado: "))
print(f"Preço total a pagar: {carRental(kilometers, days)}")