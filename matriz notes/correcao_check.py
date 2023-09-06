
#1)	Faça uma função que recebe uma matriz como parâmetro e a printa
#elemento a elemento.(1 ponto)
def printa_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz[{i}][{j}] = {matriz[i][j]}")
    return

#2)	Faça uma função que recebe uma matriz como parâmetro e printa linha a linha,
#forma que estamos mais acostumado a ver uma matriz.(1 ponto)

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return


#3)	Faça uma função que recebe o número de linhas e colunas como parâmetros e cria
#uma matriz de dimensões linhas x colunas contendo somente zeros (2 pontos)

def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(0)
    return matriz

#matriz = cria_matriz(3,4)
#mostra_matriz(matriz)
#printa_elementos(matriz)

#4)	Crie uma matriz 8x8 contendo o padrão de um tabuleiro de xadrez (2 pontos).
#Explique em um comentário no código seu raciocínio.(2 pontos)

xadrez = cria_matriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2:
            if j%2:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j%2:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0
#mostra_matriz(xadrez)

#num tabuleirode xadrez deve-se alternar as cores branco e preto a cada linha, porém
#linhas consecutivas devem ter o padrão de cor defasado, por exemplo:
#0 1 0 1
#1 0 1 0
#assim percebemos que o padrão de alternancia das cores deve iniciar com 0 em linhas
# pares e manter 0 nas colunas pares.
#o contrário deve acontecer nas linhas ímpares, ou seja, linhas impares e colunas pares
#devem ter 1, linhas impares colunas impares, 0

from time import time
def matriz_distancia(lista_x,lista_y):
    distancias = cria_matriz(len(x),len(x))
    for i in range(len(lista_x)):
        for j in range(i):
            dist_ij = round(((lista_x[i] - lista_x[j])**2 + (lista_y[i]-lista_y[j])**2)**0.5)
            distancias[i][j] = dist_ij
            distancias[j][i] = dist_ij
    return distancias


def matriz_distancia_lento(lista_x,lista_y):
    distancias = cria_matriz(len(x),len(x))
    for i in range(len(lista_x)):
        for j in range(len(lista_x)):
            dist_ij = round(((lista_x[i] - lista_x[j])**2 + (lista_y[i]-lista_y[j])**2)**0.5)
            distancias[i][j] = dist_ij
            #distancias[j][i] = dist_ij
    return distancias

x = [i for i in range(10000)]
y = [i for i in range(10000,0,-1)]
t1 = time()
matriz_dist = matriz_distancia(x,y)
t2 = time()
print(t2-t1)
#mostra_matriz(matriz_dist)

t1 = time()
matriz_dist = matriz_distancia_lento(x,y)
t2 = time()
print(t2-t1)
