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

import pandas as pd
carros = {"modelos":[], "precos":[]}
while True:
    pergunta = input("Vc quer adiocionar mais alguma coisa")
    if pergunta == "s":
        for key in carros.keys():
            info = input(f"Diga o {key}: ")
            carros[key].append(info)
    else:
        print("cadastro finalizado!")
        print(pd.DataFrame(carros))
        break




