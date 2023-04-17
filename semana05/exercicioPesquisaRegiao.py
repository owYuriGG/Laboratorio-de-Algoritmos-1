salarioTotal = 0
menorIdade = 1000
maiorIdade = 0
qtdMulheres = 0
contador = 0

idade = int(input("Digite uma idade: "))

if idade > maiorIdade:
    maiorIdade = idade
if idade < menorIdade:
    menorIdade = idade
salario = float(input("Digite um salário: "))

sexo = str(input("Digite seu sexo (masculino/feminino): ")).upper()
if sexo == "FEMININO" and salario <= 100:
    qtdMulheres += 1
salarioTotal += salario

while contador < 10:
    idade = int(input("Digite uma idade: "))
    if idade > maiorIdade:
        maiorIdade = idade
    if idade < menorIdade:
        menorIdade = idade
    salario = float(input("Digite um salário: "))
    sexo = str(input("Digite seu sexo (masculino/feminino): ")).upper()
    if sexo == "FEMININO" and salario <= 100:
        qtdMulheres += 1
    salarioTotal += salario
    contador += 1

mediaSalario = salarioTotal / 10

print(f" A média salarial do grupo é de: {mediaSalario}. \nA maior idade do grupo é de {maiorIdade}, e a menor é de {menorIdade}. \nQuantidade de mulheres com salário até R$100,00: {qtdMulheres}.")




