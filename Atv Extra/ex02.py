def km_to_mi(a):
    return a * 0.6214
def m_to_cm(a):
    return a * 100
def l_to_ml(a):
    return a * 1000

while True:
    print("Insira Quilometros:")
    km = input(">> ")
    print("Insira metros:")
    m = input(">> ")
    print("Insira litros:")
    l = input(">> ")
    
    print(f"Quilometro para milha: {km_to_mi(km)}")
    print(f"metro para centimetro: {m_to_cm(m)}")
    print(f"litro para mililitro: {l_to_ml(l)}")