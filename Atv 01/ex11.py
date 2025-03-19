while True:
    usrN = input("Envie nome de usuário: ")
    passW = input("Envie senha: ")
    
    if usrN == passW:
        print("Nome de usuário não pode ser igual a sua senha")
        break
    else:
        print("Sucesso")
        break