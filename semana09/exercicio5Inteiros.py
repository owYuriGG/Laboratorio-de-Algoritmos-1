def receberValores():
    valores = []
    for i in range (0, 5):
        n = int(input("Digite um valor: "))
        valores.append(n)
    return valores

def calcularSoma(valores):
    soma = 0
    for n in valores:
        soma += n
    return soma

def calcularMedia(valores):
    soma = 0
    for n in valores:
        soma += n
    media = soma / len(valores)
    return media

def main():
    valores = []
    valores = receberValores()
    print(calcularSoma(valores))
    print(calcularMedia(valores))

main()