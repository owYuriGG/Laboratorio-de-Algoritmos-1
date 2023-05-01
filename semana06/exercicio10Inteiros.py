#inicialização das variáveis
pares = 0
impares = 0
zeros = 0

#loop para leitura de 10 números inteiros
for i in range (1, 11):
    numero = int(input("Digite um número: "))
    if numero == 0:
        zeros += 1
    elif numero % 2 == 0:
        pares += 1
    else:
        impares += 1

#impressão dos resultados
print(f"A quantia de números pares digitados foram de: {pares}")
print(f"A quantia de números ímpares digitados foram de: {impares}")
print(f"A quantia de números zeros digitados foram de: {zeros}")