nome = str(input("Qual o seu nome? "))
salario = float(input("Qual o seu salário?"))
tempoServiço = int(input("Quanto tempo você tem de serviço:? (Em anos) "))

if tempoServiço >= 5 and salario <= 2000:
    salarioNovo = salario * 1.10
else:
    salarioNovo = salario * 1.05
print(nome, "seu novo salário será de: ", salarioNovo)