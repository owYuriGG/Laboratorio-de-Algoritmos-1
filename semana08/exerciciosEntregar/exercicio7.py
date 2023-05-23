def realizar_pesquisa():
    opnioes = []
    for i in range(20):
        opniao = input(f"Digite a opinião sobre os jornais (A, B ou C) da pessoa {i+1}: ")
        while opniao.lower() != "a" and opniao.lower() != "b" and opniao.lower() != "c":
            opniao = input("Opinião inválida. Digite novamente (A, B ou C): ")
        opnioes.append(opniao.upper())
    return opnioes

def calcular_porcentagens(opnioes):
    total = len(opnioes)
    porcentagens = {}
    for opniao in opnioes:
        if opniao in porcentagens:
            porcentagens[opniao] += 1
        else:
            porcentagens[opniao] = 1
    for key in porcentagens:
        porcentagens[key] = (porcentagens[key] / total) * 100
    return porcentagens

def main():
# Realizar a pesquisa
    print("Realize a pesquisa:")
    opnioes = realizar_pesquisa()

    # Calcular as porcentagens
    porcentagens = calcular_porcentagens(opnioes)

    # Mostrar os resultados em ordem crescente de porcentagem
    print("Resultados da pesquisa (em ordem crescente de porcentagem):")
    for key, value in sorted(porcentagens.items(), key=lambda x: x[1]):
        print(f"Jornal {key}: {value}%")

main()