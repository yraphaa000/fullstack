print("Calculo total a pagar ")
km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias: "))

total = (km * 0.15) + (dias * 60)

print(f"Total a pagar: {total:.2f}")