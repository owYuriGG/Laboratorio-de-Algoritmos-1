#Escreva um programa que cria um array com 5 números inteiros digitados pelo usuário. Em seguida, 
#encontre e exiba o maior e o menor número do array e suas respectivas posições. Obs. sem utilizar a função sort.

def receberNumeros():
    lista = []
    for i in range(5):
        n = int(input("Digite um número: "))
        lista.append(n)
    return lista

def acharMaior(lista):
    maior = 0
    posicaoMaior = 0
    contador = -1
    for i in lista:
        contador += 1
        if i > maior:
            maior = i
            posicaoMaior = contador
    return maior, posicaoMaior

def acharMenor(lista):
    menor = 1000000000000000000
    posicaoMenor = 0
    contador = -1
    for i in lista:
        contador += 1
        if i < menor:
            menor = i
            posicaoMenor = contador
    return menor, posicaoMenor


def main():
    lista = receberNumeros()
    maior, posicaoMaior = acharMaior(lista)
    menor, posicaoMenor = acharMenor(lista)
    print(f"O maior número da lista é o {maior}, na posição {posicaoMaior} da lista.")
    print(f"O menor número da lista é o {menor}, na posição {posicaoMenor} da lista.")

main()