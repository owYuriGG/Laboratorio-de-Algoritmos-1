n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print("")
print("Operações disponíveis: ")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("")

operacao =  int(input("Seleciona uma operação: "))

if operacao == 1:
    resultado = n1 + n2
elif operacao == 2:
    resultado = n1 - n2
elif operacao == 3:
    resultado = n1 * n2
elif operacao == 4:
    resultado = n1 / n2
print("Resultado: ", resultado)