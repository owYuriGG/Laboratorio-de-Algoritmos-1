lado1 = int(input("Digite o tamanho do primeiro lado do triângulo: "))
lado2 = int(input("Digite o tamanho do segundo lado do triângulo: "))
lado3 = int(input("Digite o tamanho do terceiro lado do triângulo: "))

if lado1 == lado2 and lado2 == lado3:
    print("Esse trinângulo é equilátero.")
elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
    print("Esse triângulo é isóceles.")
else:
    print("Esse triângulo é escaleno.")