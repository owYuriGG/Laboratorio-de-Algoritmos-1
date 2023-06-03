#Escreva um programa que solicita ao usuário que insira 5 números inteiros 
# e armazene-os em um array. Em seguida, calcule e exiba a soma e a média dos números.

def receberNumeros():
    lista = []
    for i in range(5):
        n = int(input("Digite um número: "))
        lista.append(n)
    return lista

def somaMedia(lista):
    media = 0
    soma = 0
    for i in lista:
        soma += i
    media = soma / 5
    return media, soma

def main():
    lista = receberNumeros()
    media, soma = somaMedia(lista)
    print(f"Média: {media}")
    print(f"Soma: {soma}")

main()