num = 2 
def par_ou_impar(numero):
    if num%2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
    return
par_ou_impar(2)
#não funciona pois, num é variavel global


#Ver se é vogal 
def e_vogal(letra):
    if letra =="a" or letra =="e" or letra =="i" or letra =="o" or letra =="u":
        print(f"{letra} é uma vogal")
    else:
        print(f"{letra} é consoante")
    return


def vogal_ou_nao(letra):
    qtd_vogais = 0
    if letra in ["a", "e", "i", "o","u"]:
        qtd_vogais = 0
        print(f"{letra} é vogal")
    else:
        print(f"{letra} é consoante")
    return qtd_vogais
    


#mini calculadora 
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

res = soma(2,3)
print(res)

res = subtracao(2,3)
print(res)

res = multiplicacao(2,3)
print(res)

res = divisao(2,3)
print(res)