def totalPrice(price):
    if (price <= 500):
        return price
    else: 
        priceWithTax = price + ((price - 500) * 0.5)
        return priceWithTax
    
print("Insira valor total das mercadorias compradas: ")
price = int(input())
print(f"Preço total da compra: {totalPrice(price)}")