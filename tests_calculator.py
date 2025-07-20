import physicsCalculator
import json

with open("./formulas.json") as f:
    formulae = json.load(f)

# testes Força
print("Teste 1 passou") if physicsCalculator.calculate(formulae["fma"], ["3", "2", ""], True) == 1.5 else print("Teste 1 falhou")
print("Teste 2 passou") if physicsCalculator.calculate(formulae["fma"], ["", "2", "1.5"], True) == 3 else print("Teste 2 falhou")
print("Teste 3 passou") if physicsCalculator.calculate(formulae["fma"], ["3", "", "1.5"], True) == 2 else print("Teste 3 falhou")

# testes Posição final 
print("Teste 4 passou") if physicsCalculator.calculate(formulae["sovt"], ["", "20", "4", "5"], True) == 40 else print("Teste 4 falhou")
print("Teste 5 passou") if physicsCalculator.calculate(formulae["sovt"], ["40", "", "4", "5"], True) == 20 else print("Teste 5 falhou")
print("Teste 6 passou") if physicsCalculator.calculate(formulae["sovt"], ["40", "20", "", "5"], True) == 4 else print("Teste 6 falhou")
print("Teste 7 passou") if physicsCalculator.calculate(formulae["sovt"], ["-20", "20", "-4", ""], True) == 10 else print("Teste 7 falhou")

# testes Velocidade
print("Teste 8 passou") if physicsCalculator.calculate(formulae["voat"], ["", "-20", "-8", "5"], True) == -60 else print("Teste 8 falhou")
print("Teste 9 passou") if physicsCalculator.calculate(formulae["voat"], ["40", "", "4", "5"], True) == 20 else print("Teste 9 falhou")
print("Teste 10 passou") if physicsCalculator.calculate(formulae["voat"], ["40", "20", "", "5"], True) == 4 else print("Teste 10 falhou")
print("Teste 11 passou") if physicsCalculator.calculate(formulae["voat"], ["-20", "20", "-4", ""], True) == 10 else print("Teste 11 falhou")
