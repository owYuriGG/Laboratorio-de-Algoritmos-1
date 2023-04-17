contador = 0

for contagem in range(1, 10):
    idade = int(input("Digite uma idade: "))
    if idade >= 18:
        contador += 1

print(f"{contador} pessoas tem idade maior ou igual a 18 anos.")
