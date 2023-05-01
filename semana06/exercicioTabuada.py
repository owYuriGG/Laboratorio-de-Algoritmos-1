#recebimento de um número
numero = int(input("Digite um número: "))

#loop para a tabuada par
print("Números pares: ")
for i in range(1, 11):
    tabuada = numero * i
    if tabuada % 2 == 0:
        print(tabuada)

print("\nNúmeros ímpares: ")
#loop para a tabuada impar
for i2 in range(1, 11):
    tabuada = numero * i2
    if tabuada % 2 == 1:
        print(tabuada)