# jogo = {'são paulo': 'vencedor', 'corinthians': 'perdedor'}
# jogo['palmeiras'] = 'sem mundial'

# time = input('Pra que time vc torce? ')
# print(f"Voce é um{jogo[time]} ")
import random 

def acha_maior(valores,nomes):
    maior = valores[0]
    local_maior = 0
    for i in range(len(valores)):
        if valores[i]>maior:
            maior = valores[i]
            local_maior = i
    return nomes[local_maior]


'''
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

'''

modelos = {'carros': ['fiesta', 'celta', 'jeep'],
           'precos': [20.000, 50.000, 40.000] }

print(acha_maior(modelos['precos'], modelos['carros']))


modelos = {'carros': ['fiesta', 'celta', 'jeep'],
           'precos': [20.000, 50.000, 40.000] }
maior = modelos['precos'][0]
indice_maior = 0 
for i in range(len(modelos['precos'])):
    if modelos['precos'][i] > maior:
        indice_maior = i
        maior = modelos['precos'][i]
print(f"O carro mais caro é o {modelos['modelo'][indice_maior]}"
      f"e custa {modelos['precos'][indice_maior]}")
