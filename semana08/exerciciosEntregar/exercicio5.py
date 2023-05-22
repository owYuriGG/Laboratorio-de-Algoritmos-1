def somaTudo(numero):
    i = 0
    contador = 0
    while i <= numero:
        contador += i
        i += 1
    return contador

somatudo = somaTudo(int(input("digite um número: ")))
print(somatudo)