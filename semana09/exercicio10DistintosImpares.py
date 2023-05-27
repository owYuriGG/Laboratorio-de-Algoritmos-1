#Faça um algoritmo que leia 10 valores distintos. Ao final apresente todos os valores somente nas posições ímpares.

def lerValores():
    valores = []
    for i in range (0, 10):
        valor = float(input("Digite um valor: "))
        valores.append(valor)
    return valores

def mostrarValores(valores):
    print(valores)
    for n in range(0, len(valores)):
        if n % 2 == 1:
            print(valores[n])

def main():
    lista = []
    lista = lerValores()
    mostrarValores(lista)


main()