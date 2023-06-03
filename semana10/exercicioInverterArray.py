#Escreva uma função em Python que recebe um array de números inteiros e retorna um novo array com os elementos na ordem inversa.

def criarLista():
    lista = []
    for i in range(5):
        n = int(input("Digite um valor: "))
        lista.append(n)
    return lista

def inverterLista(lista):
    listaInversa = []
    listaCopia = lista[:]
    for i in range(5):
        listaInversa.append(listaCopia[-1])
        listaCopia.pop(-1)
    return listaInversa

def main():
    lista = criarLista()
    listaInversa = inverterLista(lista)
    print(f"Lista inicial: {lista}")
    print(f"Lista invertida: {listaInversa}")

main()