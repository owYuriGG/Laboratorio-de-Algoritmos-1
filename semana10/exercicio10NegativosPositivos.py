#Faça  um programa que preencha um vetor com 10 números reais, 
#calcule e mostre a quantidade de números negativos e a soma dos números positivos desse vetor
import random

def criarLista():
    lista = []
    for i in range(10):
        lista.append(random.randint(-100, 100))
    return lista

def calcQuantia(lista):
    qtdNegativos = 0
    somaPositivos = 0
    for i in lista:
        if i >= 0:
            somaPositivos += i
        else:
            qtdNegativos += 1
    return qtdNegativos, somaPositivos

def main():
    lista = criarLista()
    print(lista)
    qtdNegativos, somaPositivos = calcQuantia(lista)
    print(f"A quantia de números negativos é de: {qtdNegativos} números.")
    print(f"A soma dos números positivos desse vetor é de: {somaPositivos}.")

main()