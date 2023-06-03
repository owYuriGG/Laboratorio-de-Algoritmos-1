#Escreva um programa que cria dois arrays de tamanho igual, preenchidos com números inteiros digitados pelo usuário. 
#Em seguida, crie um terceiro array que contenha a soma dos elementos correspondentes dos arrays anteriores.

def criarLista():
    lista = []
    for i in range(5):
        n = int(input("Digite um número: "))
        lista.append(n)
    return lista

def somarElementos(lista1, lista2):
    listaSomada = []
    contador = 0
    while contador < 5:
        n1 = lista1[contador]
        n2 = lista2[contador]
        soma = n1 + n2
        listaSomada.append(soma)
        contador += 1
    return listaSomada

def main():
    lista1 = criarLista()
    lista2 = criarLista()
    listaSomada = somarElementos(lista1, lista2)
    print(listaSomada)

main()