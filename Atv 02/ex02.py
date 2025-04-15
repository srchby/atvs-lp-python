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
            if product[0] == name:
                found = True
                product[1] = qty
                product[2] = price
        if not found:
            stock.append([name, qty, price])
    except ValueError:
        print("\nQuantidade ou Preço inválido\n")

def display_stock():
    if not stock:
        print("Produto não achado")
        return
    print("Estoque: \n")
    for i, product in enumerate(stock):
        print(f"{i}. Nome: {product[0]} | Quantidade: {product[1]} | Preço: {product[2]} | Valor total: {product[2] * product[1]}")
        return

load_stock()

while True:
    save_stock()
    action = int(input(f"1. Adicionar estoque \n2. Exibir estoque \n3. Sair \n"))
    
    if (action == 1):
        name = input(f"Nome do produto: \n>>")
        qty = input(f"Quantidade: \n>>")
        price = input(f"Preço: \n>>")
        add_stock(name, qty, price)
    elif (action == 2):
        display_stock()
    elif (action == 3):
        save_stock()
        break
    else:
        print("Ação inválida")