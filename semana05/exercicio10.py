numero = 1
contador = 0

while numero != 0:
    numero = int(input("Digite um número: "))
    if numero == 10:
        contador += 1

print(f"O número 10 foi digitado {contador} vezes.")