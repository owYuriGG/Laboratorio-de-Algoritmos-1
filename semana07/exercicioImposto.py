def somaImposto(taxaImposto, custo):
    custo = ((taxaImposto / 100) * custo) + custo
    return custo

custo = somaImposto(50, 100)
print(custo)
