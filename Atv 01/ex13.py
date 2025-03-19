def salary(wage, years, pct):
    for year in range(1, years + 1):
        finalWage += wage * (pct * 0.01) * (2 ** (year - 1))
    return finalWage

while True:
    wage = input("Diga um salário inicial: ")
    years = int(input("Diga os anos: "))
    pct = float(input("Diga o aumento percentual (em %): "))
    newSalary = salary(wage, years, pct)
    print(f"O seu salário de {wage} após {years} anos, é de: {newSalary}")
    break