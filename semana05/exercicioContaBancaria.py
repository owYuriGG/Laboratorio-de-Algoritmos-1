saldo = float(input("Digite o saldo inicial: "))
opcao = 0

while opcao != 4:
    print("1 - Sacar ")
    print("2 - Depositar")
    print("3 - Saldo")
    print("4 - Sair")
    opcao = int(input("Digite a opção: "))
    
    if opcao == 1:
        sacar = float(input("Digite o valor do saque: "))
        saldo -= sacar
        print(f"Valor sacado: R${sacar:,.2f}")
    elif opcao == 2:
        depositar = float(input("Digite o valor do depósito: "))
        saldo += depositar
        print(f"Valor depositado: R${depositar:,.2f}")
    elif opcao == 3:
        print(f"Saldo disponível na conta: R${saldo:,.2f}")
    elif opcao == 4:
        print("Até mais!")