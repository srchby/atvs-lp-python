def carRental(kilometers, days):
    if kilometers > 100:
        totalPrice = ((kilometers - 100) * 12) + (90 * days)
        return totalPrice
    else:
        totalPrice = 90 * days
        return totalPrice
    
print(f"Insira Quilomêtros andados e dias em que o carro foi usado: ")
kilometers = float(input())
days = input(input())
print(f"Preço total a pagar: {carRental(kilometers, days)}")