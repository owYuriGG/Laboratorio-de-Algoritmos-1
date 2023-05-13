#Funções

def notas():
    notas = []
    for i in range(5):
        nota = float(input(f"Informe a nota {i+1}: "))
        notas += [nota]
    return notas

def media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    media = soma / 5
    return media

def resultado(media):
    if media >= 7:
        return "Aprovado."
    elif media < 7 and media > 4:
        return "Recuperação."
    else:
        return "Reprovado."

notas = notas()
media = media(notas)
resultado = resultado(media)

print(f"A média do aluno é de: {media}")
print(f"O aluno está: {resultado}")