import json

green = "\033[32m"
reset = "\033[0m"
yellow = "\033[93m"
red = "\033[91m"

def calculate(formula):
    # Find which variable is empty (to be calculated)
    empty_var = None
    for var, val in formula["attributes"].items():
        if val == '':
            if empty_var is None:
                empty_var = var
            else:
                # More than one variable is empty
                raise RuntimeError("Erro: Deixe apenas uma variável em branco")
        else:
            # Convert the value to float
            formula["attributes"][var] = float(val)
            
    # Check if there is more than one empty variable
    if empty_var is None:
        raise RuntimeError("Erro: Deixe uma variável em branco para calcular")
    
    # Find the correct formula that solves for the empty variable
    target_formula = None
    for curr_formula in formula["formula"]:
        # Get the variable being solved (left side of equation)
        solved_var = curr_formula.split(" = ")[0].strip()
        if solved_var == empty_var:
            target_formula = curr_formula
            break
    
    if target_formula is None:
        return RuntimeWarning("Erro: Não foi possível encontrar fórmula para {}".format(empty_var))
    
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
        
        # Get the name and unit of the calculated variable
        var_index = list(formula["attributes"].keys()).index(empty_var)
       
        var_name = formula["names"][var_index]
        var_unit = formula["units"][var_index]
        
        return round(result, 5), var_name, var_unit
                
    except ZeroDivisionError:
        raise ZeroDivisionError("Erro: Divisão por zero")
    except Exception as e:
        raise RuntimeError(f"Erro: {e}")


def selectFormula(data, dType):
    selected = "" # Initiating a value 
    scope = range(len(data)) # Determining the scope
    while selected not in scope: # While the selected value isn't in the scope

        if selected != "": # If the value is different than initial
            print(f"Opção inválida\n") # It means you selected a wrong value

        if dType == "fórmula": # If it's a formula we display it, instead of the name
            for i, v in enumerate(data):
                print(f"{i+1}: {data[v]['formula'][0]}") 
        else:
            for i, v in enumerate(data): # Otherwise, we display the name
                print(f"{i+1}: {v}") 

        selected = int(input("Qual {} desejas usar?\n> ".format(dType))) -1 # The question itself
    return list(data)[selected] # returns the specified value

def insertValues(selected, skipLetter="#"):
    for i,v in enumerate(selected["attributes"]):
        if selected["attributes"][v] != '' or v == skipLetter:
            continue
        
        print(f"Insira o valor d{selected['names'][i]} em {selected['units'][i]} (ou deixe em branco): ")
        selected["attributes"][v] = input(f"> ")


def main():
    with open('./formulas.json') as f:
        data = json.load(f) # Load the data from the JSON
    
    category = selectFormula(data, "categoria") 
    formula = selectFormula(data[category], "fórmula")
    
    selected = data[category][formula]
    
    if "requires" in selected:
        required = selected["requires"]
        
        for value in required.keys():
            calculating = data [ required[value][0] ] [ required[value][1] ]

            insertValues(calculating, value)
            
            result, var_name, var_unit = calculate(calculating)
            
            selected["attributes"][value] = result 

    print(f"\n{yellow}Para calcular uma variável, deixe seu valor em branco{reset}")
    print("Insira os valores conhecidos normalmente\n")

    insertValues(selected)

    result, var_name, var_unit = calculate(selected)
    print(f"{green}Resultado:{reset}\n{yellow}{var_name} é de: {result:.3f} {var_unit}{reset}")

if __name__ == "__main__":
    while True:
        main()

