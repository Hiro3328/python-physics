import json

green = "\033[32m"
reset = "\033[0m"
yellow = "\033[93m"
red = "\033[91m"

def printNames():
    print("Formulas Suportadas: ")
    print(" 1: F = m*a")
    print(" 2: S = S0 + V0*t")
    print(" 3: V = V0 + a*t")

def calculate(formula, values, debug=False):
    # Reset the attributeLetters for this formula
    for letter in formula["attributes"]:
        formula["attributes"][letter] = ''
    
    # Map values to their corresponding letters based on order
    value_keys = list(formula["attributes"].keys())
    
    for i, value in enumerate(values):
        if value.strip() == '':  # Empty value
            formula["attributes"][value_keys[i]] = ''
        else:
            try:
                formula["attributes"][value_keys[i]] = float(value)
                # attributeLetters[formula][value_keys[i]] = float(value)
            except ValueError:
                return f"{red}Erro: '{value}' não é um número válido{reset}"

    # Find which variable is empty (to be calculated)
    empty_var = None
    for var, val in formula["attributes"].items():
        if val == '':
            if empty_var is None:
                empty_var = var
            else:
                return f"{red}Erro: Deixe apenas uma variável em branco{reset}"
    
    if empty_var is None:
        return f"{red}Erro: Deixe uma variável em branco para calcular{reset}"
    
    # Find the correct formula that solves for the empty variable
    target_formula = None
    for curr_formula in formula["formula"]:
        # Get the variable being solved (left side of equation)
        solved_var = curr_formula.split(" = ")[0].strip()
        if solved_var == empty_var:
            target_formula = curr_formula
            break
    
    if target_formula is None:
        return f"{red}Erro: Não foi possível encontrar fórmula para {empty_var}{reset}"
    
    # Extract the right side of the equation
    expression = target_formula.split(" = ")[1].strip()
    
    # Replace variables with their values
    sorted_vars = sorted(formula["attributes"].items(), key=lambda x: len(x[0]), reverse=True)
    for var, val in sorted_vars:
        if val != '':  # Only replace non-empty variables
            expression = expression.replace(var, str(val))
    
    # Evaluate the expression
    try:
        result = eval(expression)
        
        # print(f"\n{result:.2f} = {expression}")
        # Get the name and unit of the calculated variable
        var_index = value_keys.index(empty_var)
       
        var_name = formula["names"][var_index]
        var_unit = formula["units"][var_index]
        
        if debug:
            return result

        return f"{green}Resultado:{reset}\n{yellow}{var_name.capitalize()} é de: {result:.3f} {var_unit}{reset}"
        
    except ZeroDivisionError:
        return f"{red}Erro: Divisão por zero{reset}"
    except Exception as e:
        return f"{red}Erro no cálculo: {e}{reset}"

def main():
    # Shows the available formulae
    printNames()
    formula = "0"

    # Keep getting the selected formula while the user doesn't choose a valid one
    while formula not in ["1", "2", "3"]:
        if formula != "0": 
            print(f"{red}Opção inválida{reset}\nEscolha entre 1, 2 ou 3")
        formula = input("Qual fórmula usar?\n> ")
            
    translationMap = ["fma", "sovt", "voat"]
        
    with open('./formulas.json') as f:
        # Load the json and then select the formula using the answer 
        #                       Transforming the answer from string to int and reducing it by 1 to match the index
        selected = json.load(f)[translationMap[int(formula)-1]]
        f.close() # The file isn't needed anymore
    
    print(f"\n{yellow}Para calcular uma variável, deixe seu valor em branco{reset}")
    print("Insira os valores conhecidos normalmente\n")
    
    values = []
    for i in range(len(selected["names"])):
        prompt = f"Insira o valor de {selected['names'][i]} em {selected['units'][i]} (ou deixe em branco): "
        values.append(input(prompt + "\n> "))
    
    result = calculate(selected, values)
    print(f"\n{result}\n\n")

if __name__ == "__main__":
    while True:
        main()
