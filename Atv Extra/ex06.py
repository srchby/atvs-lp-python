def vowel_counter(a):
    vowels = ["a","e","i","o","u"]
    a = str(a)
    a.lower()
    i = 0
    for char in a:
        if vowels in char:
            i += 1
    return i

while True:
    print("Insira texto:")
    a = input(">> ")
    print(f"Quantidade de vogais: {vowel_counter(a)}")