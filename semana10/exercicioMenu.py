def menu():
    print("1 - Inserir item")
    print("2 - Listar itens")
    print("3 - Retirar itens")
    print("4 - Retirar todos os itens")
    print("5 - Sair")
    opc = int(input("Digite uma opção: "))
    return opc

def inserirItem(lista):
    n = int(input("Digite o item para adicionar a lista: "))
    if n % 2 != 0:
        print("ERRO!")
        return lista
    lista.append(n)
    return lista

def listarItens(lista):
    print(lista)

def retirarItem(lista):
    n = int(input("Digite o item a retirar da lista: "))
    lista.remove(n)
    return lista

def retirarTudo(lista):
    lista = []
    return lista

def main():
    lista = []
    opc = 0
    while opc != 5:
        opc = menu()
        if opc == 1:
            lista = inserirItem(lista)
        elif opc == 2:
            listarItens(lista)
        elif opc == 3:
            lista = retirarItem(lista)
        elif opc == 4:
            lista = retirarTudo(lista)

main()
