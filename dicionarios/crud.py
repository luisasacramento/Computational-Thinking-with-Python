'''frase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
frase = frase.replace(".",'')
frase = frase.lower()
print(frase)
print("a" == "A")
frase = frase.split(" ")
print(frase)

dic = {}
for palavra in frase:
    if palavra not in dic.keys():
        dic[palavra] = 1
    else:
        dic[palavra] += 1
print(dic)
'''
#pergunte ao usuário se ele é cliente ou funcionário
#se for cliente, de as opções de vinhos da casa e pergunte seu endereço
#pergunte informações a respeito de qual ele quer ver
#pergunte se ele vai comprar o vinho escolhido no item anterior
#caso queira, adicione ao carrinho dele o vinho e seu preço
#se for funcionário pergunte qual operação ele desja realizar
#1-Cadastrar um novo whiskey
#2-Atualizar o preço de um whiskey
#3-Atualizar o estoque de um whiskey
#4-Deletar um whiskey da tabela
lista = [10,20,30,40]
lista.remove(30)
lista.pop(2)
def obriga_opcao(msg,lista_opcoes):
    resposta = input(msg)
    if resposta not in lista_opcoes:
        print("Digite uma opção cadastrada!")
        return obriga_opcao(msg,lista_opcoes)
    return resposta
def printa_dic(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dic(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return
def checa_estoque(opcao):
    if whiskeys['estoque'][opcao] == 0:
        return False
    whiskeys['estoque'][opcao] -= 1
    return True
def cadastrar():
    for key in whiskeys.keys():
        info = input(f"Diga o/a novo/a {key} : ")
        whiskeys[key].append(info)
    print(pd.DataFrame(whiskeys))
    return
def alterar(preco_estoque):
    for i in range(len(whiskeys['tipo'])):
        print(f"{i} - {whiskeys['tipo'][i]}")
    qual = int(obriga_opcao(f"De que whiskey vc irá alterar o {preco_estoque}?",opcoes))
    novo = input(f"Diga o novo {preco_estoque}")
    whiskeys[preco_estoque][qual] = novo
    return
def remover():
    for i in range(len(whiskeys['tipo'])):
        print(f"{i} - {whiskeys['tipo'][i]}")
    qual = int(obriga_opcao(f"Qual será removido ?",opcoes))
    for key in whiskeys.keys():
        whiskeys[key].pop(qual)
    return
whiskeys = {
    'tipo' : ['bourbon', 'blended', 'scotch', 'single malt', 'double malt'],
    '% alcoólico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preço' : [100,130,20,25,50],
    'Nacionalidade' : ['chileno','argentino','françês','italiano','jundiaiense'],
    'estoque' : [1,34,54,12,11]
}
compra = {
    'endereço' : {
        'Rua' : '',
        'Cep' : '',
        'Número': ''},
    'valor total' : 0,
    'garrafas' : {}
          }
import pandas as pd
print(pd.DataFrame(whiskeys))
opcoes = [str(i) for i in range(len(whiskeys['tipo']))]
papel = obriga_opcao("Voce é cliente ou funcionário ? (c/f) ",['c','f'])
if papel == 'c':
    print("Seja bem vindo!")
    for key in compra['endereço'].keys():
        info = input(f"Diga seu/a {key}")
        compra['endereço'][key] = info
    while True:
        print("Essas são nossas opções de whiskeys : ")
        for i in range(len(whiskeys['tipo'])):
            print(f"{i} : {whiskeys['tipo'][i]}")
        opcao = int(obriga_opcao("Qual vinho lhe interessou mais ? ",opcoes))
        for key in whiskeys.keys():
            print(f"{key} : {whiskeys[key][opcao]}")
        comprar = obriga_opcao("Vai levar ? (s/n) ",['s','n'])
        if comprar == 's' and checa_estoque(opcao):
            compra['valor total'] += whiskeys['preço'][opcao]
            qual = whiskeys['tipo'][opcao]
            if qual not in compra['garrafas'].keys():
                compra['garrafas'][qual] = 1
            else:
                compra['garrafas'][qual] += 1
        elif comprar != 'n':
            print(f"Desculpe, infelizmente não há mais estoque de {whiskeys['tipo'][opcao]}")
        continuar = obriga_opcao("Quer ver mais opceos ? ",['s','n'])
        if continuar == 'n':
            print("Obrigado por comprar conosco!\nEsse é o resumo de sua compra")
            printa_dic(compra)
            break
else:
    while True:
        operacao = obriga_opcao("Qual operação vc deseja realizar:\n"
                                "1-Cadastrar novo produto\n"
                                "2-Alterar preço\n"
                                "3-Alterar estoque\n"
                                "4-Remover Produto\n"
                                "5-sair",['1','2','3','4','5'])
        if operacao == '1':
            cadastrar()
        elif operacao == '2':
            alterar('preço')
            print(pd.DataFrame(whiskeys))
        elif operacao == '3':
            alterar('estoque')
            print(pd.DataFrame(whiskeys))
        elif operacao == '4':
            remover()
            print(pd.DataFrame(whiskeys))
        else:
            break
