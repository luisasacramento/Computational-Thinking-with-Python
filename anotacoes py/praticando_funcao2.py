#muito importante

#função 
#2 parametros, listas com nomes e precos
#percorra a lista de precos e encontre o maior e seu indice
#retorne o vinho com o maior indice
def acha_maior(valores,nomes):
    maior = valores[0]
    local_maior = 0
    for i in range(len(valores)):
        if valores[i]>maior:
            maior = valores[i]
            local_maior = i
    return nomes[local_maior]

vinhos = ["tinto", "rose", "branco", "suave", "fedido", "cheiroso"]
precos = [100,200,150,75, 237,50]

maior = precos[0]
local_maior = 0
for i in range(len(precos)):
    print(f"agora testo se {precos[i]} > {maior}")
    if precos[i]>maior:
        print(f"troquei o maior de {maior} para {precos[i]}")
        maior = precos[i]
        local_maior = i
        print(f"o maior preço é {maior} e é o do vinho {vinhos[local_maior]}")

vinho_mais_caro = acha_maior(precos,vinhos)
print(vinho_mais_caro)



#paddind pesquisar 

#pedir pro usuario se ele quer saber o mais barato ou mais caro 
def checa_opcoes(frase, opcoes_cadastradas):
    operacao = input(frase)
    while not operacao in opcoes_cadastradas:
        operacao = input(frase)
        return operacao

def acha_maior(valores,nomes):
    maior = valores[0]
    local_maior = 0
    for i in range(len(valores)):
        if valores[i]>maior:
            maior = valores[i]
            local_maior = i
    return nomes[local_maior]


def acha_menor(valores,nomes):
    menor = valores[0]
    local_menor = 0
    for i in range(len(valores)):
        if valores[i]<menor:
            menor = valores[i]
            local_menor = i
    return nomes[local_menor]


vinhos = ["tinto", "rose", "branco", "suave", "fedido", "cheiroso"]
precos = [100,200,150,75, 237,50]
resposta = checa_opcoes("Voce quer encontra o maior ou o menor?")

if resposta == "maior":
    vinho_mais_caro = acha_maior(precos,vinhos)
    print(vinho_mais_caro)
else:
    vinho_mais_barato = acha_menor(precos,vinhos)
    print(vinho_mais_barato)



#Achar a média dos precos do vinho 

vinhos = ["tinto", "rose", "branco", "suave", "fedido", "cheiroso"]
precos = [100,200,150,75, 237,50]

def acha_media(valores):
    soma = 0
    for valor in valores:
        soma+= valor
    return soma/len(valores)
        

