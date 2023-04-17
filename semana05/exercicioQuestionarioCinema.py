qtdOtimo = 0
idadeOtimo = 0

qtdBom = 0
percBom = 0

qtdRegular = 0

for contagem in range(1, 15):
    print("3 - Ótimo")
    print("2 - Bom")
    print("1 - Regular\n")

    opcao = int(input("Escolha uma opção de avaliação: "))
    idade = int(input("Digite a sua idade: "))

    if opcao == 3:
        qtdOtimo += 1
        idadeOtimo += idade
    elif opcao == 2:
        qtdBom += 1
    elif opcao == 1:
        qtdRegular += 1

mediaIdadeOtimo = idadeOtimo / qtdOtimo

percBom = (qtdBom * 100) / 15

print (f"\nMédia de idade das pessoas que responderam ótimo: {mediaIdadeOtimo}.")
print (f"{qtdRegular} pessoas responderam regular.")
print (f"{percBom}% das pessoas responderam bom.\n")