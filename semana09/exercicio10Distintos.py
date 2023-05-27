def lerValores():
    valores = []
    for i in range (0, 10):
        valor = float(input("Digite um valor: "))
        valores.append(valor)
    return valores

def mostrarValores(valores):
    print(valores)

def main():
    lista = []
    lista = lerValores()
    mostrarValores(lista)

main()