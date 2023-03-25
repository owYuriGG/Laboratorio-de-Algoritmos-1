anoNasci = int(input("Digite seu ano de nascimento: "))
voto = 2023 - anoNasci

if voto >= 18:
    print("Você pode votar.")
else:
    print("Você não pode votar.")