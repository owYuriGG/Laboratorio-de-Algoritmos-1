#Faça um algoritmo que leia 10 valores distintos. Ao final apresente quantos valores são maiores que 100.

def lerValores():
    valores = []
    for i in range (0, 10):
        valor = float(input("Digite um valor: "))
        valores.append(valor)
    return valores

def mostrarValores(valores):
    contador = 0
    for n in valores:
        if n > 100:
            contador += 1
    print(f"{contador} valores são maiores que 100.")

def main():
    lista = []
    lista = lerValores()
    mostrarValores(lista)


main()