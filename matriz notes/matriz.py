
#imagem é um matriz numerica

tam = 10 
matriz = [[1 for i in range(tam)] for j in range(tam)]
for i in range(tam):
    for j in range(tam):
        if i<j:
            matriz[i][j]=0


import matplotlib.pyplot as plt
plt.imshow(matriz)
plt.colorbar()
plt.show()



#printando todos os números da matriz 

matriz = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matriz[0])):
    for j in range(len(matriz[0])):
        print(matriz[i][j])



#mudando todos para 0
matriz = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(matriz[0])):
    for j in range(len(matriz[0])):
        matriz[i][j] = 0
print(matriz)

#diagonal é i = j 
#tranformar todos os numeros abaixo da diogonal em 1
matriz = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]

#matriz = np.array(matriz)
print(matriz)
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if j<i:
            matriz[i][j] =1
            