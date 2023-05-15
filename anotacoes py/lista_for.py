#conte a quantidade de pares na lista
#modo mais 'fácil' qtd = len([par for par i numeros if par%2==0])
qtd = 0
numeros = [234, 546, 567, 523467, 2343, 54234]
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        qtd+=1
print(qtd)

#terceiro metodo 
qtd = 0 
for num in numeros:
    if num%2==0:
        qtd+=1


#printe a soma das duas listas elemento a elemento
#adicione a soma elemento a elemento a uma terceira lista
#quando quer usar as duas listas fazer for por indice
num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [11,12,13,14,15,16,17,18,19,20]
soma = []
for i in range(len(num1)):
    add = num1[i]+num2[i]
    soma.append(add)
    print(soma)



#conte a quantidade de vogais na lista

#por indice
vogais = 0 
letras = ["a", "b", "c", "d", "i","o", "h"]
for i in range(len(letras)):
    if letras[i] == "a" or letras[i] == "e" or letras[i] == "i" or letras[i] == "o" or letras[i] =="u":
        vogais+=1
print(vogais)

#por elemento
vogais = 0
for letra in letras:
    if letra in ["a", "e", "i", "o", "u"]:
        vogais +=1


# #ache a posição de danilo
profs = ["allen", "israel", "danilo", "yan", "luciano", "ana", "cordeiro"]
#codigo pra saber SE ele está na lista
i = 0
for nome in profs : 
    if nome == "danilo":
        print(f"achei o dan no indice {i}")
        indice_dan = i 
    i+=1
print(profs[indice_dan])

#outro jeito
for i in range(len(profs)):
    if profs[i] == "danilo":
        print(f"achei o dan no indice {i}")
        indice_dan = i 
print(profs[indice_dan])



#ache o carro mais caro e o mais barato
carros = ["ka", "celta", "golf", "fusca"]
preco = [10,1000, 200, 5]
maior  = preco[0]
for i in range (len(preco)):
    if preco[i]>maior:
        maior = preco[i]
        indice_maior = i
        print(f"Até o momento o maior custa {maior} no indice {indice_maior}")
print(f"o carro mais caro é o {carros[indice_maior]} e custa {preco[indice_maior]}")


#inverter a lista
lista = ["a", "b", "c", "d", "i","o", "h"]



#exemplo em aula alterando valor da lista
numeros = [0,0,0,0,0,0,0]
for elem in numeros:
    print(elem)
    elem = 1
    print(elem)
print(numeros)
for i in range(len(numeros)):
    numeros[i] = 1
print(numeros)



#Achar os numeros pares e fazer uma lista com os q não são pares
numeros = [12,234,43,54,7,234423,51,435354,5,6]
pares = 0
for elem in numeros:
    if elem%2==0:
        pares += 1
numeros_2 = [2435,56,56,34,43,2,45456,54]