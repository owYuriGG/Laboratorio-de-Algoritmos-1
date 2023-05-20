
def perc1030(idades):
    contador = 0
    for idade in idades:
        if 10 <= idade <= 30:
            contador += 1
    porcentagem = (contador / len(idades)) * 100
    return porcentagem

def maiores(idades):
    contador = 0
    for idade in idades:
        if idade >= 18:
            contador += 1
    return contador

def media(idades):
    soma = sum(idades)
    media = soma / len(idades)
    return media

def idades():
    idades = []
    for i in range(7):
        idade = int(input(f"Informe a idade da {i+1}ª pessoa: "))
        idades.append(idade)
    return idades

def main():
    idades = idades()
    media = media(idades)
    maiores = maiores(idades)
    perc1030 = perc1030(idades)

    print(f"A média das idades é: {media}")
    print(f"Quantidade de pessoas maiores de idade: {maiores}")
    print(f"Porcentagem de pessoas com idade entre 10 e 30 anos: {perc1030}%")

main()
