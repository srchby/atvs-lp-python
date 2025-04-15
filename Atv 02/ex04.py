logs = []
accounts = []
connected = False
connected_account = None

def register_account(name, key):
    global connected_account, connected
    if not name or not key:
        print("Nome ou senha inválida")
        return
    
    for acc in accounts:
        if acc[0] == name:
            print("Conta já existe")
            return
    
    accounts.append([name, key, 1000])
    print(f"Conta cadastrada")

def login_account(name, key):
    global connected_account, connected
    if not name or not key:
        print("Nome ou senha inválida")
        return
    
    for acc in accounts:
        if acc[0] == name and acc[1] == key:
            connected_account = name
            connected = True
            print("Conta conectada")
            return
        
    print("Conta não conectada")

def deposit_account(value):
    try:
        value = int(value)
        if value > 0:
            for acc in accounts:
                if acc[0] == connected_account:
                    acc[2] += value
                    print("Transação realizada com sucesso")
                    deposit_log(value)
                    return
        else: 
            print("Valor não válido")

    except ValueError:
        print("Valor não válido")
        return
def withdrawl_account(value):
    try:
        value = int(value)
        if value > 0:
            for acc in accounts:
                if acc[0] == connected_account:
                    if value > acc[2]:
                        print("Valor maior que saldo da conta")
                        return
                    acc[2] -= value
                    print("Transação realizada com sucesso")
                    withdrawl_log(value)
                    return
        else: 
            print("Valor não válido")
    except ValueError:
        print("Valor não válido")
        return
def deposit_log(value):
    log = f"Transação: Déposito de {value} na conta de {connected_account}"
    logs.append(log)
def withdrawl_log(value):
    log = f"Transação: Saque de {value} na conta de {connected_account}"
    logs.append(log)
def show_logs():
    for log in logs:
        print(f"{log}\n")

while True:
    if not connected or connected_account is None:
        action = input("Conta não conectada \n1. Login \n2. Cadastrar \n3. Sair \n>> ")
        if action == "1":
            name = input("Insira nome: \n>> ")
            key = input("Insira senha: \n>> ")
            login_account(name, key)
            if connected:
                print("Conta conectada")
        elif action == "2":
            name = input("Insira nome: \n>> ")
            key = input("Insira senha: \n>> ")
            register_account(name, key)
            if connected:
                print("Conta registrada")
        elif action == "3":
            break
        else:
            print("Ação inválida")
    else:
        action = input(f"Conta: {connected_account} \n1. Depositar \n2. Sacar \n3. Transações \n4. Sair\n>> ")
        
        if action == "1":
            value = input("Insira quantidade para depositar: \n>> ")
            deposit_account(value)
        elif action == "2":
            value = input("Insira Quantidade para sacar: \n>> ")
            withdrawl_account(value)
        elif action == "3":
            for log in logs:
                print(f"{log}\n")
        elif action == "4":
            connected = False
            connected_account = None
            print("Desconectado")