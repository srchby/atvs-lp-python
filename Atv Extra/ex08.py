def palindrome_checker(a):
    if a == a[::-1]:
        return True
    else: 
        return False
    
while True:
    print("Insira palavra: ")
    word = input(">> ")
    answer = palindrome_checker(word)
    if (answer == True):
        print("É um palíndromo")
    else: 
        print("Não é um palíndromo")