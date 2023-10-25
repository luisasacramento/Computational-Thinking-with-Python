def acha_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        candidato = lista[i]
        if candidato < menor:
            menor = candidato
            indice_menor = i
    return indice_menor
def selection_sort_pior(lista):
    ordenada = []
    while lista:
        indice = acha_menor(lista)
        menor = lista.pop(indice)
        ordenada.append(menor)
        print(lista)
        print(ordenada)
        print()
    return ordenada
lista  = [4,2,6,1,7,8,0]
print(lista[3:])
selection_sort_pior([4,2,6,1,7,8,0])
