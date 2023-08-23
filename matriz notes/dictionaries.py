# jogo = {'são paulo': 'vencedor', 'corinthians': 'perdedor'}
# jogo['palmeiras'] = 'sem mundial'

# time = input('Pra que time vc torce? ')
# print(f"Voce é um{jogo[time]} ")
import random 

saudacoes = {'oi':['olá', 'salve', 'e ai', 'fmz'], 
            'tchau': ['e o pix', 'flw',  'tmj', 'vaza']
            }
print(saudacoes.keys())
while True:
    resposta = input('Diga oi ou tchau: ')
    if resposta in saudacoes.keys():
        print(random.choice(saudacoes[resposta]))
    elif resposta == 'sair':
        break
    else:
        print("fala dnv")



parentes = {}
parentes['mae'] = 'fabiana'
parentes['vó'] = 'vera'
parentes['pai'] = 'fabio'
parentes['irmao'] = 'gabriel'
parentes['tio'] = 'felipe'
for key in parentes.keys():
    print(f"O nome do/a seu/sua {key} é {parentes[key]}")

