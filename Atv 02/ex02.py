import json

stock = []

def load_stock():
    global stock
    try:
        with open("stock.json", "r") as infile:
            stock = json.load(infile)
    except FileNotFoundError:
        stock = []
        
def save_stock():
    with open("stock.json", "w") as outfile:
        json.dump(stock, outfile, indent=4)

def add_stock(name, qty, price):
    try:
        qty = int(qty)
        price = float(price)
        
        found = False
        for product in stock:
            if product["name"] == name:
                found = True
                product["quantity"] = qty
                product["price"] = price
                break
        if not found:
            stock.append({
                "name": name,
                "quantity": qty,
                "price": price
            })
    except ValueError:
        print("\nQuantidade ou Preço inválido\n")

def display_stock():
    if not stock:
        print("Produto não achado")
        return
    print("Estoque: \n")
    for i, product in enumerate(stock):
        total_value = product["price"] * product["quantity"]
        print(f"{i}. Nome: {product['name']} | Quantidade: {product['quantity']} | Preço: {product['price']} | Valor total: {total_value}")

load_stock()

while True:
    save_stock()
    action = input("1. Adicionar estoque \n2. Exibir estoque \n3. Sair \n>> ")
    
    if action == "1":
        name = input("Nome do produto: \n>> ")
        qty = input("Quantidade: \n>> ")
        price = input("Preço: \n>> ")
        add_stock(name, qty, price)
    elif action == "2":
        display_stock()
    elif action == "3":
        save_stock()
        break
    else:
        print("Ação inválida")