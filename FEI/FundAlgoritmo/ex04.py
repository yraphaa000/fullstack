print("Calcular salario")
valorHr = float(input("Digite o valor da hora de trabalho: "))
nHr= float(input("Digite o numero de horas trabalhadas: "))

salarioBruto = valorHr * nHr
ir = salarioBruto * 0.11
inss = salarioBruto *0.08
sindicato = salarioBruto * 0.05

salarioLiquido = salarioBruto - (ir + inss + sindicato)

print(f"Salario bruto {salarioBruto}")

