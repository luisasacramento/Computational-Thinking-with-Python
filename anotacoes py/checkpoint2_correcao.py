print("Bem-Vindo!!")

endereco = input("Diga seu endereço : ")
ano = input("Diga seu ano de nascimento : ")
while not ano.isnumeric():
    ano = input("seu ano de nascimento deve ser numero: ")
ano=int(ano)

if 2023 - ano < 18:
    print("que feio não pode")
else: 
    valor = 0 
    qtd_tinto = 0 
    qtd_suave = 0 
    qtd_rose = 0 
    while True:
        opcao = input("Qual vinhio voce quer? (tinto, suave, rosé")
        while not (opcao == "tinto" or opcao == "suave" or opcao =="rosé"):
           opcao = input("tem que ser uma dessas: (tinto, suave, rosé) ")
    
        qtd = input(f"quantas garrafas de {opcao} vc quer? ")
        while not qtd.isnumeric():
           qtd = input(f"Qts garrafas de {opcao} vc quer?")
        qtd = int(qtd)

        if opcao == "tinto":
           valor+=30*qtd
           qtd_tinto += qtd
        elif opcao == "suave":
           valor+=40*qtd
           qtd_suave +=qtd
        else:
           valor+=50*qtd
           qtd_rose += qtd
        pergunta = input("Voce quer continuar comprando? (s/n)")
        while not (pergunta == "s" or pergunta == "n"):
             pergunta = input("Voce que continuar comprando? (s/n)")
        if pergunta == "s":
            continue
        else:
            break
if valor > 500: 
    print("Voce recebeu frete grátis!")
else:
    valor +=10
print(f"Valeu, vc gastou R${valor},00 em {qtd_suave} suave, \n"
f"{qtd_tinto} tinto e {qtd_rose} rosé, \n"
f"e será entregue em {endereco}")