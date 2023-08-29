import random

def mostra_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    return


def cria_matriz_aleatoria(linhas, colunas):
    matriz = []
    for i in range(linhas):
        matriz.append([])
        # print(matriz)
        for j in range(colunas):
            matriz[i].append(random.randint(0,10))
    return matriz


print("MULTIPLICAÇÃO")
# matriz_pesos = cria_matriz(1,5)
def soma_lista(lista):
    soma = 0
    for elem in lista:
        soma+=elem
    return soma

def soma_elementos(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma


alunos = 10
notas = cria_matriz_aleatoria(5,alunos)
pesos = [1,2,3,2,1]
soma_pesos = soma_elementos(pesos)
medias = []
mostra_matriz(notas)
for j in range(alunos):
    soma = 0
    for i in range(len(pesos)):
        soma += pesos[i]*notas[i][j]
    media = soma/soma_pesos
    medias.append(media)
print(medias)