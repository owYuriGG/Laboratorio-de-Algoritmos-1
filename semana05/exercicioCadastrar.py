alturaGeral = 0
idadeGeral = 0
qtdPessoas = 0

print("--- Menu ---")
print("1 - Cadastrar pessoa")
print("2 - Mostrar média parcial")
print("3 - Sair")

opcao = int(input("Digite a opção: "))

while opcao != 3:
    if opcao == 1:
        idade = int(input("Digite a idade: "))
        idadeGeral += idade
        altura = float(input("Digite a altura: "))
        alturaGeral += altura
        qtdPessoas += 1
        print("\n")
    elif opcao == 2:
        mediaTempIdade = idadeGeral / qtdPessoas
        mediaTempAltura = alturaGeral / qtdPessoas
        print(f"A idade média atual é de: {mediaTempIdade} anos e a altura média é de {mediaTempAltura:}cm. \n")
        print("--- Menu ---")
    print("1 - Cadastrar pessoa")
    print("2 - Mostrar média parcial")
    print("3 - Sair")
    opcao = int(input("Digite a opção: "))
    

mediaIdadeFinal = idadeGeral / qtdPessoas
mediaAlturaFinal = alturaGeral / qtdPessoas

print(f"A média final de idade é de {mediaIdadeFinal} anos e a média final de altura é de {mediaAlturaFinal}cm.")