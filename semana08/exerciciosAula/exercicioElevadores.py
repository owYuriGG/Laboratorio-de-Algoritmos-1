#Em um prédio com 10 moradores há três elevadores denominados A, B e C. Para otimizar o sistema de controle dos elevadores, 
#desenvolva um programa em que cada morador informa qual o elevador que utiliza com mais frequência (A, B ou C). 
#O algoritmo deve contabilizar o total de pessoas que usa cada um dos elevadores e mostrar estes totais e 
#suas respectivas porcentagens no final.
#Use funções!

def contagemElevadores():
    elevadorA = 0
    elevadorB = 0
    elevadorC = 0

    for i in range(10):
        elevador = input(f"Informe o elevador utilizado pelo {i+1}º morador (A, B ou C): ").upper()

        if elevador == 'A':
            elevadorA += 1
        elif elevador == 'B':
            elevadorB += 1
        elif elevador == 'C':
            elevadorC += 1

    return elevadorA, elevadorB, elevadorC

def porcentagens(elevadorA, elevadorB, elevadorC):
    qtdPessoas = elevadorA + elevadorB + elevadorC
    porcentagemA = (elevadorA / qtdPessoas) * 100
    porcentagemB = (elevadorB / qtdPessoas) * 100
    porcentagemC = (elevadorC / qtdPessoas) * 100

    return porcentagemA, porcentagemB, porcentagemC


def main():
    elevadorA, elevadorB, elevadorC = contagemElevadores()
    porcentagemA, porcentagemB, porcentagemC = porcentagens(elevadorA, elevadorB, elevadorC)

    print(f"Total de pessoas que utilizam o elevador A: {elevadorA} ({porcentagemA}%)")
    print(f"Total de pessoas que utilizam o elevador B: {elevadorB} ({porcentagemB}%)")
    print(f"Total de pessoas que utilizam o elevador C: {elevadorC} ({porcentagemC}%)")

main()
