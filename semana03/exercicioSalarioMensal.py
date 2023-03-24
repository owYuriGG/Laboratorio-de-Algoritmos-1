horasTrab = int(input("Digite a quantia de horas trabalhadas: "))
salario = horasTrab * 35

if salario < 1000:
    salario = salario + 300
    print("O salário será de: ", salario)
else:
    print("O salário será de: ", salario)
