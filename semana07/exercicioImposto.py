def somaImposto(taxaImposto, custo):
    custo = ((taxaImposto / 100) * custo) + custo
    return custo

def main():
    custo = somaImposto(50, 100)
    print(custo)

main()
