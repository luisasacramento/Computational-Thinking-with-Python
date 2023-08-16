def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return


def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        for j in range(colunas):
            matriz[i].append(i)
    return matriz


'''
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
'''

xadrez = cria_matriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[0])):
        if i%2==j%2:
            xadrez[i][j] = 0
        else:
            xadrez[i][j] = 1          
mostra_matriz(xadrez)



