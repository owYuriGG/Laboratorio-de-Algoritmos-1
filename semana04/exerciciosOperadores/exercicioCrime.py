telefonou = str(input("Você telefonou para a vítima? (Sim/Não) ")).upper()
local = str(input("Você esteve no local do crime? (Sim/Não) ")).upper()
mora = str(input("Você mora perto da vítima? (Sim/Não) ")).upper()
devia = str(input("Você devia para a vítima? (Sim/Não) ")).upper()
trabalhou = str(input("Você trabalhou para a vítima? (Sim/Não) ")).upper()

placar = 0

if telefonou == "SIM":
    placar = placar + 1

if local == "SIM":
    placar = placar + 1

if mora == "SIM":
    placar = placar + 1

if devia == "SIM":
    placar = placar + 1

if trabalhou == "SIM":
    placar = placar + 1

if placar == 5:
    print("Classificação: Assassino.")
elif placar == 4 or placar == 3:
    print("Classificação: Cúmplice.")
elif placar == 2:
    print("Classificação: Suspeita.")
elif placar == 1 or placar == 0:
    print("Classificação: Inocente.")