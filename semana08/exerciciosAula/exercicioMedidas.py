def decimetros(valor):
    valorDecimetros = valor * 10
    return valorDecimetros

def centimetros(valor):
    valorCentimetros = valor * 100
    return valorCentimetros

def milimetros(valor):
    valorMilimetros = valor * 1000
    return valorMilimetros

def main():
    valor = float(input("Digite um valor em metros: "))
    print(f"{valor} metros em decímetros é: {decimetros(valor)} decímetros")
    print(f"{valor} metros em centímetros é: {centimetros(valor)} centímetros")
    print(f"{valor} metros em milímetros é: {milimetros(valor)} milímetros")

main()
