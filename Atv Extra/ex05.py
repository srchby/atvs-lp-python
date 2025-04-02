def table(a):
    i = 1
    while i <= 10:
        print(f"{a} * {i}: {a * i}")
        i += 1

while True:
    print("Coloque número: ")
    a = int(input(">> "))
    table(a)