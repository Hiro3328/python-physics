green = "\033[32m"
reset = "\033[0m"
yellow = "\033[93m"
red = "\033[91m"

namesDictionarys = {
    "fma":  ["a força", "a massa", "a aceleração"],
    "sovt": ["a posição final", "a posição inicial", "a velocidade", "o tempo"],
    "voat": ["a velocidade final", "a velocidade inicial", "a aceleração", "o tempo"],
}

unitsDictionarys = {
    "fma":  ["N", "Kg", "m/s²"],
    "sovt": ["m", "m", "m/s", "s"],
    "voat": ["m/s", "m/s", "m/s²", "s"],
}

formulae = {
    "fma":  ["F = m*a", "m = F/a", "a = F/m"],
    "sovt": ["S = S0 + V*t", "S0 = S - V*t", "V = (S - S0)/t", "t = (S - S0)/V"], 
    "voat": ["V = V0 + a*t", "V0 = V - a*t", "a = (V - V0)/t", "t = (V - V0)/a"], 
}

attributeLetters = {
    "fma":  {"F": '', "m": '', "a": ''},
    "sovt": {"S": '', "S0": '', "V": '', "t": ''},
    "voat": {"V": '', "V0": '', "a": '', "t": ''},
}

def printNames():
    print("Formulas Suportadas: ")
    print(" 1: F = m*a")
    print(" 2: S = S0 + V0*t")
    print(" 3: V = V0 + a*t")

def calculate(formula, values):
    # Redefine os valores em attributeLetters para esta fórmula
    for letter in attributeLetters[formula]:
        attributeLetters[formula][letter] = ''
    
    # Cria uma lista com as letras da fórmula selecionada 
    value_keys = list(attributeLetters[formula].keys())
    
    # Pega ambos o índice e o valor da lista 
    for i, value in enumerate(values):
        if value.strip() == '':  
            attributeLetters[formula][value_keys[i]] = ''
        else:
            # tenta transformar o valor em um número
            try:
                attributeLetters[formula][value_keys[i]] = float(value)
            except ValueError:
                # se nao conseguir ele mostra o erro
                return f"{red}Erro: '{value}' não é um número válido{reset}"

    # Encontra qual variável está vazia (a que será calculada)
    empty_var = None
    for var, val in attributeLetters[formula].items():
        if val == '':
            if empty_var is None:
                empty_var = var
            else:
                return f"{red}Erro: Deixe apenas uma variável em branco{reset}"
    
    if empty_var is None:
        return f"{red}Erro: Deixe uma variável em branco para calcular{reset}"
    
    # Encontra a fórmula correta que resolve para a variável vazia
    target_formula = None
    for curr_formula in formulae[formula]:
        # Separa a variável que está sendo resolvida ( a parte da esquerda da equação)
        solved_var = curr_formula.split(" = ")[0].strip()
        if solved_var == empty_var:
            target_formula = curr_formula
            break
    
    if target_formula is None:
        return f"{red}Erro: Não foi possível encontrar fórmula para {empty_var}{reset}"
    
    # Extrai a parte da direita da equação
    expression = target_formula.split(" = ")[1].strip()
    
    # Troca as letras por seus respectivos valores
    sorted_vars = sorted(attributeLetters[formula].items(), key=lambda x: len(x[0]), reverse=True)
    for var, val in sorted_vars:
        if val != '':  # Troca apenas valores não vazios
            expression = expression.replace(var, str(val))
    
    # Executa a expressão "como se fosse um código em python"
    try:
        result = eval(expression)
        
        print(f"\n{result:.2f} = {expression}")
        # Pega o nome e a unidade da variável calculada
        var_index = value_keys.index(empty_var)
        var_name = namesDictionarys[formula][var_index]
        var_unit = unitsDictionarys[formula][var_index]
        
        return f"{green}Resultado:{reset}\n{yellow}{var_name.capitalize()} é de: {result:.3f} {var_unit}{reset}"
        
    except ZeroDivisionError:
        return f"{red}Erro: Divisão por zero{reset}"
    except Exception as e:
        return f"{red}Erro no cálculo: {e}{reset}"

def main():
    # Mostra as fórmulas disponíveis
    printNames()
    formula = "0"

    # Enquanto o usuário não selecionar uma fórmula válida 
    while formula not in ["1", "2", "3"]:
        if formula != "0": 
            print(f"{red}Opção inválida{reset}\nEscolha entre 1, 2 ou 3")
        formula = input("Qual fórmula usar?\n> ")
            
    translationMap = {
        "1": "fma",
        "2": "sovt",
        "3": "voat",
    }
    selected = translationMap[formula] # pra transformar o número que ele escolheu no nome da fórmula
    
    print(f"\n{yellow}Para calcular uma variável, deixe seu valor em branco{reset}")
    print("Insira os valores conhecidos normalmente\n")
    
    values = []
    # Usa os nomes das unidades pra evitar fazer um print específico para cada item 
    for i in range(len(namesDictionarys[selected])):
        prompt = f"Insira o valor de {namesDictionarys[selected][i]} em {unitsDictionarys[selected][i]} (ou deixe em branco): "
        values.append(input(prompt + "\n> "))
    
    result = calculate(selected, values)
    print(f"\n{result}\n\n")

# Jeito do python de dizer pra só executar isso se for chamado diretamente
# Fiz para poder adicionar testes sem eu ter que ficar mexendo no arquivo
if __name__ == "__main__":
    while True:
        main()
