print("Loja de Roupas VESTOSA!")
valorRoupa = float(input("Digite o valor da peça: "))

print("")
print("Opções de pagamento: ")
print("1 - Á vista. ")
print("2 - 2 vezes. ")
print("3 - 3 vezes. ")
print("")

opcao = int(input("Digite a opção de pagamento: "))

if opcao == 1:
    parcela = valorRoupa / 1
    print("O valor de pagamento á vista será de: ", parcela, "reais. ")
elif opcao == 2:
    parcela = valorRoupa / 2
    print("O valor das parcelas será de: ", parcela, "reais. ")
elif opcao == 3:
    parcela = valorRoupa / 3
    print("O valor das parcelas será de: ", parcela, "reais. ")
else:
    print("Digite uma opção válida. ")
