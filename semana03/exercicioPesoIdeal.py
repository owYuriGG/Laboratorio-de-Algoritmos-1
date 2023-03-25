sexo = str(input("Qual seu sexo? (Masculino/Feminino) ")).upper()
altura= float(input("Qual a sua altura? "))

if sexo == "MASCULINO":
    pesoIdeal = (72.7 * altura) - 58
    print("Seu peso ideal é de: ", pesoIdeal)
else:
    pesoIdeal = (62.1 * altura) - 44.7
    print("Seu peso ideal é de: ", pesoIdeal)