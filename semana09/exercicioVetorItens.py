def menu():
    print("1 - Inserir item")
    print("2 - Retirar item")
    print("3 - Listar itens")
    print("4 - Sair")
    opc = int(input("Escolha uma opção: "))
    return opc

def inserirItem(lista):
    item = int(input("Digite um item: "))
    lista.append(item)
    return lista

def retirarItem(lista):
    item = int(input("Digite o item para retirar: "))
    lista.remove(item)
    return lista

def listarItens(lista):
    print(lista)

def main():
    opc = 0
    lista = []
    while opc != 4:
        opc = menu()
        if opc == 1:
            lista = inserirItem(lista)
        elif opc == 2:
            lista = retirarItem(lista)
        elif opc == 3:
            listarItens(lista)

main()
