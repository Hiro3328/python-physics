import json 

with open('./formulas.json') as f:
    data = json.load(f)

cat = "Astronomia"
formula = "fgm"
selected = data[cat][formula]

def insertValues(selected, data, skipLetter="#"):
    print(f"\nPara calcular uma variável, deixe seu valor em branco")
    print("Insira os valores conhecidos normalmente\n")
    
    attributes = selected["attributes"]
    for i,v in enumerate(attributes):
        if ":" in attributes[v]:
            requires = attributes[v].split(":")

            calculating = data [ requires[0] ] [ requires[1] ]

            print(calculating)

            insertValues(calculating, data,  v)



        if attributes[v] != '' or v == skipLetter:
            continue
        
        print(f"Insira o valor de {selected['names'][i]} em {selected['units'][i]} (ou deixe em branco): ")
        attributes[v] = input(f"> ")
insertValues(selected, data)

print(selected["attributes"])
