import random


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

matriz1 = cria_matriz(8,8)
for i in range(len(matriz1)):
     for j in range(len(matriz1[0])):
         if j%2==0:
             matriz1[i][j] = 1
mostra_matriz(matriz1)

