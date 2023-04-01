qtdMorango = float(input("Digite a quantia de Kg's de morangos comprados: "))
qtdMacas = float(input("Digite a quantia de Kg's de maças compradas: "))

kgTotal = qtdMorango + qtdMacas

if qtdMorango < 5:
    valorMorango = qtdMorango * 2.50
elif qtdMorango >= 5:
    valorMorango = qtdMorango * 2.20

if qtdMacas < 5:
    valorMacas = qtdMacas * 1.80
elif qtdMacas >= 5:
    valorMacas = qtdMacas * 1.50

valorGeral = valorMacas + valorMorango

if valorGeral >= 25.00 or kgTotal >= 8:
    valorTotal = valorGeral * 0.90
else:
    valorTotal = valorGeral

print("O valor total da compra será de: ", valorTotal)
