#Escreva um programa que cria um array com 10 números inteiros aleatórios no intervalo de 1 a 50. 
#Em seguida, exiba a quantidade de números pares e a quantidade de números ímpares no array.
import random

def criarLista():
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 50))
    return lista

def calcQuantias(lista):
    somaPares = 0
    somaImpares = 0
    for i in lista:
        if i % 2 == 0:
            somaPares += 1
        else:
            somaImpares += 1
    return somaPares, somaImpares

def main():
    lista = criarLista()
    print(lista)
    somaPares, somaImpares = calcQuantias(lista)
    print(f"A quantia de números pares na lista é de: {somaPares}")
    print(f"A quantia de números ímpares na lista é de: {somaImpares}")

main()