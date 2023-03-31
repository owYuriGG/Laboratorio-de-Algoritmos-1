n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print("O número ", n1, "é o maior número.")
    print("O número ", n2, "é o menor número.")
elif n1 < n2:
    print("O número ", n2, "é o maior número.")
    print("O número ", n1, "é o menor número.")
elif n1 == n2:
    print("Os dois números são iguais.")