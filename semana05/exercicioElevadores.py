qtdA = 0
qtdB = 0
qtdC = 0

for contagem in range(0, 10):
    opcao= str(input("Qual elevador você usa com mais frequência? A, B ou C? ")).upper()
    if opcao == "A":
        qtdA += 1
    elif opcao == "B":
        qtdB += 1
    elif opcao =="C":
        qtdC += 1

percA = (qtdA * 100) / 10
percB = (qtdB * 100) / 10
percC = (qtdC * 100) / 10

print(f" {percA}% dos moradores utilizam o elevador A. \n {percB}% dos moradores utilizam o elevador B. \n {percC}% dos moradores utilizam o elevador C.")