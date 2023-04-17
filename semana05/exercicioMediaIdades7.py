qtdPessoas = 0
idadeGeral = 0
qtdHomens = 0
idadeHomens = 0
qtdMulheres = 0
idadeMulheres = 0

for contagem in range(1, 7):
    idade = int(input("Digite uma idade: "))
    sexo = str(input("Digite seu sexo (masculino/feminino): ")).upper()
    if sexo == "MASCULINO":
        qtdHomens += 1
        idadeHomens += idade
    elif sexo == "FEMININO":
        qtdMulheres += 1
        idadeMulheres += idade
    qtdPessoas += 1
    idadeGeral += idade

idadeMediaGeral = idadeGeral / qtdPessoas
idadeMediaHomens = idadeHomens / qtdHomens
idadeMediaMulheres = idadeMulheres / qtdMulheres

print(f" A idade média do grupo é de {idadeMediaGeral}. \n A idade média das mulheres é de {idadeMediaMulheres}. \n A idade média dos homens é de {idadeMediaHomens}.")
