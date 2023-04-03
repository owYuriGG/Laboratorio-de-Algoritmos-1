nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

frequencia = int(input("Digite a frequência de presenças: "))

if media >= 7 and frequencia >= 75:
    print("Você foi aprovado!")
elif media >= 4 and frequencia > 75:
    print("Você está em exame!")
elif media < 4 or frequencia <= 75:
    print("Você está reprovado!")
