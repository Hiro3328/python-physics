print("Calculadora F = m*a")
letraEscolhida = input("qual das letras você quer calcular?\n> ")

if letraEscolhida.lower() == "f":
    massa = float(input("Insira o valor da massa em Kg: "))
    aceleracao = float(input("Insira o valor da aceleração em m/s²: "))
    print("A força é de {}N".format(aceleracao*massa))
elif letraEscolhida.lower() == "m":
    forca = float(input("Insira o valor da força em N: " ))
    aceleracao = float(input("Insira o valor da aceleração em m/s²: "))
    print("A massa é de {}Kg".format(forca/aceleracao))
elif letraEscolhida.lower() == "a":
    massa = float(input("Insira o valor da massa em Kg: "))
    forca = float(input("Insira o valor da força em N: "))
    print("A aceleração é de {}m/s²".format(forca/massa))


