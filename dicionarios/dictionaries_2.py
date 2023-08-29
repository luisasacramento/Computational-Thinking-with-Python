def acha_maior(lista):
    indice_maior = 0
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i]>maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

dict_um = {"brasileirao":7,
           "copa do brasil":3, 
           "fundação":1910, 
           "paulista":30}

for key in dict_um.keys():
    print(f"o nome do seu time{key}:{dict_um[key]}")



numeros = {"pares":[], "impares":[]}
for i in range(10):
    if i%2==0:
        numeros["pares"].append(i)
    else:
        numeros["impares"].append(i)
print(numeros)

modelos = {'carros': ['fiesta', 'celta', 'jeep'],
           'precos': [20.000, 50.000, 40.000] }

print(acha_maior(modelos['precos'], modelos['carros']))


modelos = {'carros': ['fiesta', 'celta', 'jeep'],
           'precos': [20.000, 50.000, 40.000] }
pergunta = input('Quer cadstrar mais um carro')
maior = modelos['precos'][0]
indice_maior = 0 
for i in range(len(modelos['precos'])):
    if modelos['precos'][i] > maior:
        indice_maior = i
        maior = modelos['precos'][i]
print(f"O carro mais caro é o {modelos['modelo'][indice_maior]}"
      f"e custa {modelos['precos'][indice_maior]}")



