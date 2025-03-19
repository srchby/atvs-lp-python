def biggestNum(a, b, c):
    arr = []
    arr.extend([a, b, c])
    
    j = arr[0]
    for i in range(0, len(arr)):
        if arr[i] > j:
            j = arr[i]
            
    return j

def smallestNum(a, b, c):
    arr = []
    arr.extend([a, b, c])
    
    j = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < j:
            j = arr[i]
            
    return j

while (True):
    num1 = int(input("Envie três números: "))
    num2 = int(input())
    num3 = int(input())
    
    print(f"O maior número entre eles é: {biggestNum(num1, num2, num3)}")
    print(f"O menor número entre eles é: {smallestNum(num1, num2, num3)}")
    break