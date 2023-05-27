#Escreva um programa que cria um array com 5 valores inteiros digitados pelo usuário. Em seguida, solicite ao usuário que digite um número e verifique se esse número está presente no array.

def receberValores():
    valores = []
    for i in range (0, 5):
        n = int(input("Digite um valor: "))
        valores.append(n)
    return valores

def verificarNumeros(valores):
    valor = int(input("Digite um valor para verificar se o mesmo está na lista: "))
    contador = 0
    for n in valores:
        if n == valor:
            contador += 1
    if contador >= 1:
        print("O valor digitado está presente na lista.")
    else:
        print("O valor digitado não está na lista. ")

def main():
    valores = []
    valores = receberValores()
    verificarNumeros(valores)

main()  