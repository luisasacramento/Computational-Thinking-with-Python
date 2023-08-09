'''
lista = ["Danilo", "allen", "Cordeiro", "israel", "Francisco"]

for i in range(len(lista)):
    print(f"o {lista[i]} está no indice {i}")

senha = "12345"
senha_usuario = input("Diga sus senha: ")
tentativas = 1
while senha_usuario != senha and tentativas<3:
    print("errooou")
    senha_usuario = input("Diga sua senha: ")
    tentativas +=1 
if senha == senha_usuario:
    print("acesso liberado")
else:
    print("sai hacker")


for i in range(3):
    senha_usuario: input("Diga sua senha: ")
    if senha == senha_usuario:
        print("acesso liberado")

'''

lista = ["Danilo", "allen", "Cordeiro", "israel", "Francisco"]

if "Danilo" in lista:
    print(True)
    print(lista.index("Danilo"))


for nome in lista:
    if nome == "Danilo":
        print("Encontrei")

i=0
for nome in lista:
    if nome == "Danilo":
        print("Encontrei no {i}")
    i+=1

'''
carros = ["up", "ka", "celta", "uno", "kombi"]
precos = [50,100,100000,200, 300]
indice_maior = 0

maior = precos[indice_maior]
for i in range(len(precos)):
    if precos[i] > maior:
        maior = precos[i]
        indice_maior = i
print(f"o carro mais caro é o {carros[indice_maior]} e vale R${precos[indice_maior]}")



def acha_maior(valores):
    indice_maior = 0
    maior = valores[indice_maior]
    for i in range(len(valores)):
        if valores[i]> maior:
            maior = valores[i]
            indice_maior =i
    return indice_maior

lista1 = ["Maça", "Banana", "Abacaxi", "Chocolate"]
lista2 = ["Morango", "Uva", "Chocolate", "Pera"]
'''

lista1 = [1,2,3,4,5]
lista2 = [4,5,6,7,8]
comuns = []
for i in range(len(lista1)):
    for j in range(len(lista2)):
        print(f"esto verificando se {lista1[i]} == {lista2[j]} ")
        if lista1[i]==lista2[j]:
            print("achei")
            comuns.append(lista1[i])
print(comuns)


def intersecao(lista1,lista2):
    comuns = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]==lista2[j]:
                comuns.append(lista[i])
    return comuns


lista = [1,2,3,4,5,6,7,8,9]
print(lista)
ultimo = len(lista) - 1
for i in range(len(lista)//2):
    aux = lista[i]
    lista[i] = lista[ultimo-i]
    lista[ultimo-i] = aux
    print(lista)


def inverte_lista(lista):
    ultimo = len(lista) - 1
    for i in range(len(lista)//2):
        aux = lista[i]
        lista[i] = lista[ultimo-i]
        lista[ultimo-i] = aux
    return lista

