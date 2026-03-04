print("Conversor de tempo")
dias = int(input("Digite a quantidades de dias: "))
horas = int(input("Digite a quantidades de horas: "))
minutos = int(input("Digite a quantidades de minutos: "))
segundos = int(input("Digite a quantidades de segundos: "))

TempoTotal = (dias * 86400) + (horas*3600) + (minutos*60) + segundos

print(f"Tempo total foi de : {TempoTotal:.0f}")