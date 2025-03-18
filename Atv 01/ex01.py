def average(n1, n2, n3):
    avg = (n1 + n2 + n3) / 3
    return avg

def weightedAverage(n1, n2, n3, a, b, c):
    weightAvg = (n1*a + n2*b + n3*c) / 3
    return weightAvg

print("Insira três notas: ")

n1 = int(input()) 
n2 = int(input()) 
n3 = int(input()) 

print(f"Média Aritmética: {average(n1, n2, n3)}")
print(f"Média Ponderada 1: {weightedAverage(n1, n2, n3, 2, 2, 3)}")
print(f"Média Ponderada 2: {weightedAverage(n1, n2, n3, 1, 2, 2)}")