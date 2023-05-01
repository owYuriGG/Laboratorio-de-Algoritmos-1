#inicialização das variáveis
qtdA = 0
qtdB = 0
qtdC = 0

#laço de repetição do questionário
for contador in range(1, 21):
    print("Escolha o seu jornal favorito: ")
    print("1 - Jornal A")
    print("2 - Jornal B")
    print("3 - Jornal C")
    escolha = int(input("Escolha uma das opções: "))
    if escolha == 1:
        qtdA += 1
    elif escolha == 2:
        qtdB += 1
    elif escolha == 3:
        qtdC += 1

#calculo das porcentagens
percA = (qtdA * 100) / 20
percB = (qtdB * 100) / 20
percC = (qtdC * 100) / 20

#verificação da maior porcentagem
if percA > percB and percA > percC:
    print(f"A porcentagem de pessoas que leem o Jornal A é de: {percA}%.")
elif percB > percA and percB > percC:
    print(f"A porcentagem de pessoas que leem o jornal B é de: {percB}%.")
elif percC > percB and percC > percA:
    print(f"A porcentagem de pessoas que leem o jornal C é de: {percC}%.")
else:
    print("falha")

#verificação da porcentagem média
if percA > percB and percA < percC or percA < percB and percA > percC:
    print(f"A porcentagem de pessoas que leem o jornal A é de: {percA}%.")
elif percB > percA and percB < percC or percB < percA and percB > percC:
    print(f"A porcentagem de pessoas que leem o jornal B é de: {percB}%.")
elif percC > percA and percC < percB or percC < percA and percC > percB:
    print(f"A porcentagem de pessoas que leem o jornal C é de: {percC}%.")
else:
    print("falha")

#verificação da menor porcentagem
if percA < percB and percA < percC:
    print(f"A porcentagem de pessoas que leem o jornal A é de: {percA}%.")
elif percB < percA and percB < percC:
    print(f"A porcentagem de pessoas que leem o jornal B é de: {percB}%.")
elif percC < percA and percC < percB:
    print(f"A porcentagem de pessoas que leem o jornal C é de: {percC}%.")
else:
    print("falha")