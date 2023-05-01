#inicialização das variáveis
qtdNumeros = 0
soma = 0
maior = "NAO"

#verificação se o primeiro número é menor que o segundo
while maior != "SIM":
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))
    if n1 < n2:
        maior = "SIM"
    else:
        print("O primeiro número deve ser menor que o segundo!")

#laço de repetição para a soma
for i in range (n1, n2 + 1):
    soma += i
    qtdNumeros += 1

#cálculo da média
media = soma / qtdNumeros

#print da média
print(f"A média nos números no intervalo é de: {media}")