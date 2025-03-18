def secondsToMinutes(seconds):
    minutes = seconds / 60
    return minutes

def secondsToHours(seconds):
    hours = seconds / 3600
    return hours

def secondsToDays(seconds):
    hours = seconds / 86400
    return hours

print("Insira valor em segundos: ")
sec = int(input())
print(f"Em dias: {secondsToDays(sec)}")
print(f"Em horas: {secondsToHours(sec)}")
print(f"Em minutos: {secondsToMinutes(sec)}")