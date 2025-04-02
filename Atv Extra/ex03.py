def char_in_sentence(a):
    sentence = str(a)
    sentence = sentence.replace(" ",'')
    return len(sentence)

while True:
    print("Insira texto:")
    txt = input(">> ")
    print(f"Caracteres: {char_in_sentence(txt)}")