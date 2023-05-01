#inicialização das variáveis
maiorIdade = 0
qtdMulheres = 0
qtdHomens = 0
qtdOlhosAzul = 0
qtdOlhosVerde = 0
qtdOlhosCastanhos = 0
qtdCabelosLoiros = 0
qtdCabelosCastanhos = 0
qtdCabelosPretos = 0
qtdMulherVerdeLoira = 0

#loop de entrevista

for i in range(1, 16):
    #perguntas iniciais
    sexo = str(input("Qual seu sexo? (M/F): ")).upper
    if sexo == "M":
        qtdHomens += 1
    elif sexo == "F":
        qtdMulheres += 1
    
    corOlhos = str(input("Qual a cor de seus olhos? (A, V ou C): ")).upper
    if corOlhos == "A":
        qtdOlhosAzul += 1
    elif corOlhos == "V":
        qtdOlhosVerde += 1
    elif corOlhos == "C":
        qtdOlhosCastanhos += 1
    
    corCabelo = str(input("Qual a cor de seus cabelos? (L, C ou P): ")).upper
    if corCabelo == "L":
        qtdCabelosLoiros += 1
    elif corCabelo == "C":
        qtdCabelosCastanhos += 1
    elif corCabelo == "P":
        qtdCabelosPretos += 1
    
    idade = int(input("Qual a sua idade? "))
    if idade > maiorIdade:
        maiorIdade = idade
    
    #verificação quantidade de indivíduos do sexo feminino, 
    #cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos louros
    if idade in range(18, 35) and corOlhos == "V" and corCabelo == "L":
        qtdMulherVerdeLoira += 1

#cálculo das porcentagens
percOlhosAzul = (qtdOlhosAzul * 100) / 15
percOlhosVerde = (qtdOlhosVerde * 100) / 15
percOlhosCastanhos = (qtdOlhosCastanhos * 100) / 15
percCabelosLoiros = (qtdCabelosLoiros * 100) / 15
percCabelosCastanhos = (qtdCabelosCastanhos * 100) / 15
percCabelosPretos = (qtdCabelosPretos * 100) / 15
percHomem = (qtdHomens * 100) / 15
percMulher =  (qtdMulheres * 100) / 15

#impressão dos resultados
print(f"A maior idade do grupo é de: {maiorIdade}")
print(f"A quantidade de indivíduos do sexo feminino, cuja idade está entre 18 e 35 anos e que tenham olhos verdes e cabelos louros é de: {qtdMulherVerdeLoira}")
print(f"Porcentagem de pessoas com os olhos Azuis: {percOlhosAzul}%.")
print(f"Porcentagem de pessoas com os olhos Verdes: {percOlhosVerde}%.")
print(f"Porcentagem de pessoas com os olhos Castanhos: {percOlhosCastanhos}%.")
print(f"Porcentagem de pessoas com os cabelos Loiros: {percCabelosLoiros}%.")
print(f"Porcentagem de pessoas com os cabelos Pretos: {percCabelosPretos}%.")
print(f"Porcentagem de pessoas com os cabelos Castanhos: {percCabelosCastanhos}%.")
print(f"Porcentagem de homens: {percHomem}%.")
print(f"Porcentagem de mulheres: {percMulher}%.")