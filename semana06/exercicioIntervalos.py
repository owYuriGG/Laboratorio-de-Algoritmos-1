#inicialização das variáveis
qtdIntervalo = 0
qtdForaIntervalo = 0

#laço de repetição
for i in range (1, 11):
    n = int(input("Digite um número: "))
    if n > 10 and n < 20:
        qtdIntervalo += 1
    else:
        qtdForaIntervalo += 1

#impressão do resultado
print(f"A quantidade de números no intervalo de 10 a 20 é de: {qtdIntervalo} números.")
print(f"A quantidade de números fora do intervalo de 10 a 20 é de: {qtdForaIntervalo} números.")