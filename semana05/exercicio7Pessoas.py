qtdPessoas = 0
qtdMaiores = 0
qtdPerc1030 = 0
idadeTotal = 0

for contagem in range(0, 7, 1):
    idade = int(input("Digite uma idade: "))
    idadeTotal = idadeTotal + idade
    if idade >= 18:
        qtdMaiores += 1
    if idade > 10 and idade < 30:
        qtdPerc1030 += 1
    print(qtdMaiores)

perc1030 = (qtdPerc1030 * 100) / 7
mediaIdade = idadeTotal / 7

print(f"A média geral das idades é de {mediaIdade}, {qtdMaiores} pessoas são maiores de idade, e {perc1030}% tem entre 10 e 30 anos.")
