def printa_elementos(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f"matriz [{i}] [{j}] = {matriz[i][j]}")
    return

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


#altera as linhas pares
matriz1 = cria_matriz(10,10)
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if i%2 ==0:
            matriz1[i][j]=1
mostra_matriz(matriz1)

print()

#altera as colunas impares
matriz1 = cria_matriz(10,10)
for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
        if j%2 ==0:
            matriz1[i][j]=2
mostra_matriz(matriz1)

print()

#altera as colunas impares
matriz1 = cria_matriz(10,10)
for j in range(1,len(matriz1[0]),2):
    for i in range(len(matriz1)):
            matriz1[i][j]=2
        
import matplotlib.pyplot as plt
plt.imshow(matriz1)
plt.colorbar()
plt.show()
mostra_matriz(matriz1)


#for de fora e oq fca fixo e de dentro oq varia
#i para linha
#j para coluna 



#Soma de duas Matrizes

m1 = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
mostra_matriz(m1)
print()
m2 = cria_matriz(3,4)
mostra_matriz(m2)
print()
def soma (m1,m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        for i in range (len(m1)):
            for j in range(len(m1[0])):
                m1[i][j]+=m2[i][j]
        return m1
    else:
        print("impossivel somar matrizes de tamanhos distintos")
        return 
m1 = soma(m1,m2)
mostra_matriz(m1)



triangular = cria_matriz(10,10)
mostra_matriz(triangular)
for i in range (len(triangular)):
    for j in range(len(triangular[0])):
        if i >j:
            triangular[i][j] = 1

print()
mostra_matriz(triangular)