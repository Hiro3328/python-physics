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
        print(f"Teste {formula} falhou")


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

