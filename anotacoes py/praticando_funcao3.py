#salários e imposto de renda 

def i_erre (salarios):
    for salario in salarios:
        if salario <2122:
            print(f"o IR de R${salario} é isento")
        elif salario< 2826:
            print(f"o IR de R${salario} é 7,5%")
        elif salario< 3751:
            print(f"o IR de R${salario} é 15%")
        elif salario< 4664:
            print(f"o IR de R${salario} é 22,5%")
        else:
            print(f"o IR de R${salario} é 27,5%")
    return

salarios = [1000, 10000, 1500, 3000, 4000]







def checa_opcoes(frase, opcoes_cadastradas):
    resposta = input(frase)
    while not resposta in opcoes_cadastradas:
        resposta = input(frase)
    return resposta

resposta = checa_opcoes("Qual das nossas opçoes vc quer", ["a", "b", "c", "d", "e", "f"])



var = input("deseja continuar ou encerrar? ")
opcoes = ["continuar", "encerrar"]
while not var in opcoes:
    var = input("deseja continuar ou encerrar? ")




#função generica para verificar 
def verifica_opcoes(msg, lista_opcoes):
    var = input(msg)
    while not var in lista_opcoes:
        print("ERROU")
        var = input(msg)
    return var
        
opcoes = ["continuar", "encerrar"]