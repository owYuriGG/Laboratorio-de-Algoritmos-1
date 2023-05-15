#Inicialização das variáveis

#Funções
def menu():
    print("1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostrar saldo")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção:"))
    return opcao

def sacar(saldo):
    saque = float(input("Digite a quantia que deseja sacar: "))
    if saque <= saldo:
        saldo -= saque
        print(f"Novo saldo: R$ {saldo}")
        return saldo
    else:
        print("Saldo insuficiente! ")

def depositar(saldo):
    deposito = float(input("Digite a quantia do depósito: "))
    saldo += deposito
    print(f"Seu novo saldo é de: R$ {saldo}")
    return saldo

def mostrarSaldo(saldo):
    print(f"Seu saldo é de: R$ {saldo}")

def main():
    opcao = 0
    saldo = 0.0
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            saldo = sacar(saldo)
        elif opcao == 2:
            saldo = depositar(saldo)
        elif opcao == 3:
            saldo = mostrarSaldo(saldo)
        
#Código principal

main()
