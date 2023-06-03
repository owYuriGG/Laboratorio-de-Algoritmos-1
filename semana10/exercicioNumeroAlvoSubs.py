#Escreva uma função em Python que recebe um array de números inteiros, um número alvo e um número de substituição. 
#A função deve substituir todos os elementos do array que são iguais ao número alvo pelo número de substituição.

def criarLista():
    lista = []
    for i in range(5):
        n = int(input("Digite um número: "))
        lista.append(n)
    print(f"Lista inicial: {lista}")
    return lista

def subsAlvo(lista):
    alvo = int(input("Digite o valor alvo: "))
    substituto = int(input("Digite o valor de substituição: "))
    for i in range(len(lista)):
        if lista[i] == alvo:
            lista[i] = substituto
    print(f"Lista final: {lista}")
    return lista

def main():
    lista = criarLista()
    lista = subsAlvo(lista)

main()