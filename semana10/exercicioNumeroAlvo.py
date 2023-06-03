#Escreva uma função em Python que recebe um array de números inteiros e um número alvo, 
#e retorna a quantidade de elementos no array que são iguais ao número alvo.

def receberLista():
    lista = []
    for i in range(5):
        n = int(input("Digite um numero: "))
        lista.append(n)
    return lista

def acharAlvo(lista):
    contador = 0
    alvo = int(input("Digite o valor alvo: "))
    for i in lista:
        if i == alvo:
            contador += 1
    return contador

def main():
    lista = receberLista()
    qtdElementos = acharAlvo(lista)
    print(f"A quantia de elementos na array igual ao alvo é de: {qtdElementos}")

main()