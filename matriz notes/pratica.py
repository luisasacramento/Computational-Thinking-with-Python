def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        # print(matriz)
        for j in range(colunas):
            matriz[i].append((0))
    return matriz


matriz1 = cria_matriz(5,10)
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if i%2 ==0:
            matriz1[i][j]=1
mostra_matriz(matriz1)

print()

matriz2 = cria_matriz(5,10)
for i in range(len(matriz2)):
    for j in range(len(matriz2[0])):
        if j%2 ==0:
            matriz2[i][j]=1
mostra_matriz(matriz2)

print()

xadrez = cria_matriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2==0:
            if j%2==0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j%2==0:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0
mostra_matriz(xadrez)

print()
