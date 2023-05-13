#Inicialização das variáveis
saldo = 0

#Funções
def menu():
    print("1 - Sacar dinheiro")
    print("2 - Depositar dinheiro")
    print("3 - Mostrar saldo")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção:"))
    return opcao

def sacar():
    saque = float(input("Digite a quantia que deseja sacar: "))
    if saque <= saldo:
        saldo -= saque
        print(f"Novo saldo: R$ {saldo}")
    else:
        print("Saldo insuficiente! ")

def depositar():
    deposito = float(input("Digite a quantia do depósito: "))
    saldo += deposito
    return saldo

def mostrarSaldo():
    print(f"Seu saldo é de: R$ {saldo}")

def main():
    opcao = 0
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            sacar()
        elif opcao == 2:
            depositar()
        elif opcao == 3:
            mostrarSaldo()
        
#Código principal

main()