import physicsCalculator
import json

def addTest(categoria, formula, values, expected):
    with open("./formulas.json") as f:
        form = json.load(f)[categoria][formula]
        f.close()
    
    for i, v in enumerate(form["attributes"]):
        form["attributes"][v] = values[i]

    result = physicsCalculator.calculate(form)

    if result == expected:
        print(f"Teste {formula} passou")
    else:
        print(f"Teste {formula} falhou, result: {result}, expected: {expected}")


print("Primeira lei de Newton")
addTest("Física Básica","fma", ["3", "2", ""], (1.5, 'a aceleração', 'm/s²'))
addTest("Física Básica","fma", ["3", "", "1.5"], (2, 'a massa', 'Kg'))
addTest("Física Básica","fma", ["", "2", "1.5"], (3, 'a força', 'N'))

print("-------------------------")
 

print("Posição final")
addTest("Física Básica","sovt", ["", "20", "4", "5"], (40, 'a posição final', 'm'))
addTest("Física Básica","sovt", ["40", "", "4", "5"], (20, 'a posição inicial', 'm'))
addTest("Física Básica","sovt", ["40", "20", "", "5"], (4, 'a velocidade', 'm/s'))
addTest("Física Básica","sovt", ["-20", "20", "-4", ""], (10, 'o tempo', 's'))

print("-------------------------")


print("Velocidade final")
addTest("Física Básica","voat", ["", "-20", "-8", "5"], (-60, 'a velocidade final', 'm/s'))
addTest("Física Básica","voat", ["40", "", "4", "5"], (20, 'a velocidade inicial', 'm/s'))
addTest("Física Básica","voat", ["40", "20", "", "5"], (4, 'a aceleração', 'm/s²'))
addTest("Física Básica","voat", ["-20", "20", "-4", ""], (10, 'o tempo', 's')) 


print("-------------------------")
print("Gravidade")
addTest("Astronomia","gGmr", ["6.6743e-11", "", "5.972e24", "6.371e6"], (9.81997, 'a gravidade', 'm/s²')) 
addTest("Astronomia","gGmr", ["6.6743e-11", "9.819973426224687", "", "6.371e6"], (5.972e24, 'a massa', 'kg')) 
addTest("Astronomia","gGmr", ["6.6743e-11", "9.819973426224687", "5.972e24", ""], (6.371e6, 'o raio', 'm'))

print("-------------------------")
print("Velocidade de Escape")
addTest("Astronomia", "v2gmr", ["", "6.6743e-11", "5.972e24", "6.371e6"], (11185.97789, 'a velocidade', 'm/s'))
addTest("Astronomia", "v2gmr", ["617788.44071", "6.6743e-11", "", "6.96e8"], (1.990000000018921e+30, 'a massa', 'kg'))
addTest("Astronomia", "v2gmr", ["617788.44071", "6.6743e-11", "1.99e+30", ""], (695999999.99338, 'o raio', 'm'))
