def teste_numerico(frase):
    var = input(frase)
    while not var.isnumeric():
        var = input(frase)
    var = int(var)
    return var

def soma(num1, num2):
    soma = num1+num2
    return soma
def subtracao(num1, num2):
    subtracao = num1-num2
    return subtracao
def multiplicacao(num1, num2):
    multiplicacao = num1 * num2
    return multiplicacao
def divisao(num1, num2):
    divisao = num1/num2
    return divisao

def checa_opcoes(frase, opcoes_cadastradas):
    operacao = input(frase)
    while not operacao in opcoes_cadastradas:
        operacao = input(frase)
        return operacao

operacao = checa_opcoes(["soma", "subtracao", "mutiplicacao", "divisao"])
num1 = teste_numerico("Qual o primeiro numero")
num2 = teste_numerico("Qual o segundo numero")


if operacao == "soma":
    print(soma(num1,num2))
elif operacao == "subtracao":
    print(subtracao(num1,num2)) 
elif operacao == "multiplicacao":
    print(multiplicacao(num1,num2)) 
else: 
    print(divisao(num1, num2)) 








# def teste_numerico(frase):
#     var = input(frase)
#     while not var.isnumeric():
#         var = input(frase)
#     var = int(var)
#     return var

# def soma(num1, num2):
#     soma = num1+num2
#     return soma
# def subtracao(num1, num2):
#     subtracao = num1-num2
#     return subtracao
# def multiplicacao(num1, num2):
#     multiplicacao = num1 * num2
#     return multiplicacao
# def divisao(num1, num2):
#     divisao = num1/num2
#     return divisao



# num1 = teste_numerico("Qual o primeiro numero")
# num2 = teste_numerico("Qual o segundo numero")


# pergunta = input("Qual operação voce quer fazer")
# if pergunta == "soma":
#     print(soma(num1,num2))
# elif pergunta == "subtracao":
#     print(subtracao(num1,num2))
# elif pergunta == "multiplicacao":
#     print(multiplicacao(num1,num2))
# else:
#     print(divisao(num1, num2))





