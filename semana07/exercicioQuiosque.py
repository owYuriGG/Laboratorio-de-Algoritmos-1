#Funções
def valor(laranjas):
    if laranjas > 12:
        preco = laranjas * 0.25
    else:
        preco = laranjas * 0.40
    return preco

def main():
    laranjas = int(input("Digite a quantia de laranjas compradas: "))
    preco = (valor(laranjas))
    print(f"O preço da compra ficou: R$ {preco} reais.")

#Código principal
main()
