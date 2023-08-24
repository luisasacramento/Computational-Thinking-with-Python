def acha_maior(lista):
    indice_maior = 0
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i]>maior:
            maior = lista[i]
            indice_maior = i
    return indice_maior

def soma_elementos(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    return soma