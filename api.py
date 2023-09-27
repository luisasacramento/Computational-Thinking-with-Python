import pandas as pd
#pergunte ao usuÃ¡rio se ele Ã© cliente ou funcionÃ¡rio
#se for cliente, de as opÃ§Ãµes de vinhos da casa e pergunte seu endereÃ§o
#pergunte informaÃ§Ãµes a respeito de qual ele quer ver
#pergunte se ele vai comprar o vinho escolhido no item anterior
#caso queira, adicione ao carrinho dele o vinho e seu preÃ§o
def login():
    usuario = obriga_opcao("Diga seu usuario : ",["Danilo"],3)
    if usuario:
        senha = obriga_opcao("Diga sua senha : ",['1234'],3)
    else:
        return False
    return senha and usuario

def altera_preco():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    vinho = int(obriga_opcao("De que vinho vc vai alterar ? ",lista_vinhos))
    preco = float(input("Diga o novo preÃ§o : "))
    vinhos['preÃ§o'][vinho] = preco
    return
def remove_produto():
    for i in range(len(vinhos['tipo'])):
        print(f"{i} - {vinhos['tipo'][i]}")
    vinho = int(obriga_opcao("Qual vinho vc vai remover ? ",lista_vinhos))
    for key in vinhos.keys():
        vinhos[key].pop(vinho)
    return
def cadastra_produto():
    for key in vinhos.keys():
        info = input(f"Diga o/a novo/a {key} : ")
        vinhos[key].append(info)
    return
def obriga_opcao(msg,lista_opcoes,max_tentativas = None):
    resposta = input(msg)
    tentativas = 1
    while resposta not in lista_opcoes:
        print("Digite uma opÃ§Ã£o vÃ¡lida! ")
        resposta = input(msg)
        if max_tentativas:
            if tentativas>=max_tentativas-1:
                print("Sai Hacker")
                return False
            tentativas +=1
    return resposta
def printa_dicionarios(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printa_dicionarios(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return
vinhos = {
    'tipo' : ['tinto', 'rosÃ©', 'seco', 'branco', 'suave'],
    '% alcoÃ³lico' : [11,15,12,13,10],
    'safra' : [1958,1962,1970,1994,2002],
    'preÃ§o' : [100,130,20,25,50],
    'Nacionalidade' : ['chileno','argentino','franÃ§Ãªs','italiano','jundiaiense'],
    'estoque' : [1,20,30,40,50]
}
compra = {
    'valor total' : 0,
    'endereÃ§o' : {
        'cep' : '',
        'numero' : ''
    },
    'vinhos' : {}
}
printa_dicionarios(compra)
print(pd.DataFrame(vinhos))
c_f = obriga_opcao("Voce Ã© cliente ou funcionÃ¡rio ? (c/f) ",['c','f'])
lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
#lista_opcoes = []
#for i in range(len(vinhos['tipo'])):
#    lista_opcoes.append(str(i))

if c_f == 'c':
    print("Seja bem vindo!!! ")
    for key in compra['endereÃ§o'].keys():
        info = input(f"Diga seu {key} : ")
        compra['endereÃ§o'][key] = info
    while True:
        print("Essas sÃ£o nossas opÃ§Ãµes de vinhos: ")
        for i in range(len(vinhos['tipo'])):
            print(f"{i} - {vinhos['tipo'][i]}")
        opcao = int(obriga_opcao("Por qual vc se interesou ?",lista_vinhos))
        for key in vinhos.keys():
            print(f"{key} : {vinhos[key][opcao]}")
        comprar = obriga_opcao("Voce quer levar ?(s/n)",['s','n'])
        if comprar == 's':
            if vinhos['estoque'][opcao]==0:
                print(f"Desculpa, nÃ£o temos mais estoque de {vinhos['tipo'][opcao]}")
                continue
            else:
                vinhos['estoque'][opcao]-=1
            compra['valor total'] += vinhos['preÃ§o'][opcao]
            nome = vinhos['tipo'][opcao]
            if nome not in compra['vinhos'].keys():
                compra['vinhos'][nome] = 1
            else:
                compra['vinhos'][nome] += 1

        continuar = obriga_opcao("Vc quer ver mais vinhos?(s/n) ",['s','n'])
        if continuar == 'n':
            print("Obrigado pela sua compra:")
            printa_dicionarios(compra)
            break
else:
    if login():
        while True:
            operacao = obriga_opcao("Qual operacao vc deseja realizar ?\n0-Alterar preÃ§o"
                                    "\n1-Remover produto\n2-Cadastrar produto"
                                    "\n3-Sair\n-> ",['0','1','2','3'])
            if operacao == '0':
                altera_preco()
            elif operacao == '1':
                remove_produto()
                lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
            elif operacao == '2':
                cadastra_produto()
                lista_vinhos = [str(i) for i in range(len(vinhos['tipo']))]
            else:
                print("OperaÃ§Ã£o realizada com sucesso!")
                print(pd.DataFrame(vinhos))
                break
    else:
        print("Encerrando programa!")