ROWS = 5
COLUMNS = 5
map = [['L' for _ in range(COLUMNS)] for _ in range(ROWS)]

def show_seats():
    for i, row in enumerate(map):
        print(" ".join(row))
    print("\nLegenda: 'L' = Disponível | 'X' = Não Disponível")
    
def book_seat(seat):
    row = int(seat[0]) - 1
    col = int(seat[1]) - 1
    try:
        if map[row][col] == "X":
            print(f"Assento {seat} já reservado.")
        else:
            map[row][col] = "X"
            print(f"Assento {seat} reservado.")
    except (ValueError, IndexError):
        print("Assento inválido.")
        
def cancel_seat(seat):
    row = int(seat[0]) - 1
    col = int(seat[1]) - 1
    try:
        if map[row][col] == "L":
            print(f"Assento {seat} já disponível.")
        else:
            map[row][col] = "L"
            print(f"Assento {seat} disponível.")
    except (ValueError, IndexError):
        print("Assento inválido.")

while True: 
    action = input("\n1. Visualizar \n2. Reservar \n3. Cancelar \n4. Sair \n>> ")
    
    if action == "1":
        show_seats()
    elif action == "2":
        seat = input(f"Insira número do assento (11 - {ROWS}{COLUMNS}): \n>> ")
        book_seat(seat)
    elif action == "3":
        seat = input(f"Insira número do assento (11 - {ROWS}{COLUMNS}): \n>> ")
        cancel_seat(seat)
    elif action == "4":
        break
    else: 
        print("Ação inválida")