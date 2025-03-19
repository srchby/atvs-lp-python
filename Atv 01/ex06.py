def hundPrimeNum():
    i = 0
    num = 2
    while i < 100:
        if all(num % p != 0 for p in range(2, int(num**0.5) + 1)):
            print(num, end=" ")
            i += 1
        num += 1
        
hundPrimeNum()