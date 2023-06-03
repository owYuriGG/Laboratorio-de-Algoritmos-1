#Escreva um programa que cria um array com 10 números inteiros aleatórios no intervalo de 1 a 100. 
#Em seguida, exiba apenas os números pares. Utilize a função rand
import random

def criarLista():
    lista = []
    for i in range(10):
        lista.append(random.randint(1, 100))
    return lista

def printarPares(lista):
    for i in lista:
        if i % 2 == 0:
            print(f"- {i}")

def main():
    lista = criarLista()
    printarPares(lista)

main()