def criarLista():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return lista

def mostrarInverso(lista):
    contador = len(lista) - 1
    while contador > -1:
        print(f" - {lista[contador]}")
        contador -= 1

def main():
    lista = criarLista()
    mostrarInverso(lista)

main()