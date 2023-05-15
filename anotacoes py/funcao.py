def teste_numerico(frase):
    var = input(frase)
    while not var.isnumeric():
        var = input(frase)
    var = int(var)
    return var

print("Bem vindo a vinheria!!!")
endereco = input("Diga seu endereco : ")
ano = teste_numerico("Diga seu ano de nascimento : ")
if 2023 - ano < 18:
    print("que feio não pode")
else:
    valor = 0
    qtd_suave = 0
    qtd_tinto = 0
    qtd_rose = 0
    while True:
        opcao = input("Qual vinho vc quer ? (tinto, suave, rosé) ")
        while not (opcao == "tinto" or opcao == "suave" or opcao == "rosé"):
            opcao = input("tem que ser uma dessas : (tinto, suave, rosé) ")
        qtd = teste_numerico(f"Qts garrafas vc quer? ")
        if opcao == "tinto":
            valor+=30*qtd
            qtd_tinto += qtd
        elif opcao == "suave":
            valor+=40*qtd
            qtd_suave += qtd
        else:
            valor+=50*qtd
            qtd_rose += qtd
        pergunta = input("Voce quer continuar comprando ? (s/n) ")
        while not (pergunta == "s" or pergunta == "n"):
            pergunta = input("Voce quer continuar comprando ? (s/n) ")
        if pergunta == "s":
            continue
        else:
            break
    if valor > 500:
        print("Voce recebeu frete grátis!")
    else:
        valor += 10
    print(f"Valeu, vc gastou R${valor},00 em {qtd_suave} suave,\n"
          f"{qtd_tinto} tinto e {qtd_rose} rosé,\n"
          f"e será entregue em {endereco}")
    


def teste_numerico(frase,tentativas):
    var = input(frase)
    i=0
    while not var.isnumeric() and i<tentativas:
        var = input(frase)
        i+=1
    var = int(var)
    return var
def teste_par(num):
    if num%2==0:
        return True
    else:
        return False
for i in range(10):
    numero = teste_numerico("Diga um numero : ",7)
    if teste_par(numero):
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")

numeros = [12,234,43,54,7,234423,51,435354,5,6]
for numero in numeros:
    if teste_par(numero):
        print(f"{numero} é par")
    else:
        print(f"{numero} é impar")