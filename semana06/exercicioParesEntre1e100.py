#inicialização das variáveis
qtdPares = 0

#laço de repetição de verificação de números pares
for i in range(1, 101):
    if i % 2 == 0:
        qtdPares += 1

#impressão da quantia de números pares encontrados
print(f"A quantia de números pares encontrados foi de: {qtdPares} números.")