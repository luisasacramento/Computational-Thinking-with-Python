import random 

def acha_maior(lista):
    indice_maior = 0
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i]>maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

def cria_matriz_aleatoria(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        # print(matriz)
        for j in range(colunas):
            matriz[i].append(random.randint(0,10))
    return matriz

def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append((0))
    return matriz

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def transpoe_matriz(m):
    for i in range(len(m)):
        for j in range(i):
            aux = m[i][j]
            m[i][j]= m[j][i]
            m[j][i] = aux

    return mostra_matriz(m)

matriz1 = cria_matriz_aleatoria(3,3)
mostra_matriz(matriz1)
print()
transpoe_matriz(matriz1)