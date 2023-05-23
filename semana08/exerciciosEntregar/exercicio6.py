def realizar_pesquisa():
    respostas = []
    for i in range(20):
        resposta = input(f"Digite a resposta (sim ou não) da pessoa {i+1}: ")
        while resposta.lower() != "sim" and resposta.lower() != "nao":
            resposta = input("Resposta inválida. Digite novamente (sim ou não): ")
        respostas.append(resposta.lower())
    return respostas

def calcular_resultados(respostas):
    sim = respostas.count("sim")
    nao = respostas.count("nao")
    return sim, nao

def main():
    # Realizar a pesquisa
    print("Realize a pesquisa:")
    respostas = realizar_pesquisa()

    # Calcular os resultados
    sim, nao = calcular_resultados(respostas)

    # Mostrar os resultados
    print("Resultados da pesquisa:")
    print("Total de pessoas que responderam sim:", sim)
    print("Total de pessoas que responderam não:", nao)

main()