contador = 0

for contagem in range(1, 10):
    numero = int(input("Digite um número: "))
    if numero > 30 and numero < 90:
        contador += 1

print(f"{contador} números digitados estão entre 30 e 90.")