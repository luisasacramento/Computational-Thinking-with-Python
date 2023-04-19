#Resto na divisão por 2
#6 = 3*2 + 0, isso quer dizer que 6%2=0
#7 = 3*2 + 1, isso quer dizer que 7%2=1
#8 = 4*2 + 0, isso quer dizer que 8%2=0
#9 = 4*2 + 1, isso quer dizer que 9%2=1

#Resto na divisao por 3
#6 = 2*3 + 0, isso quer dizer que 6%3=0
#7 = 2*3 + 1, isso quer dizer que 7%3=1
#8 = 2*3 + 2, isso quer dizer que 8%3=2
#9 = 3*3 + 0, isso quer dizer que 9%3=0

#Resto na divisao por 4
#6 = 1*4 + 2, isso quer dizer que 6%4=2
#7 = 1*4 + 3, isso quer dizer que 7%4=3
#8 = 2*4 + 0 isso quer dizer que 8%4=0
#9 = 2*4 + 1, isso quer dizer que 9%4=1

'''
num = int(input("Diga um numero : "))
if num%2 == 0:
    print("é par")
else:
    print("é ímpar")
#receba um numero do usuario e se ele for divisível por 3, printe "é divisivel", caso contrário, printe o valor do resto
num = int(input("Diga um número : "))
#div = int(input("Diga por quanto voce quer saber se ele é divisível : "))
if num%3==0:
    print(f"O número {num} é dívisivel por 3")
else:
    print(f"O número {num} tem resto {num%3} na divisão por 3, isso quer dizer que {num}={num//3}*3+{num%3}")
'''
#receba dois numeros do usuario. O primeiro é o numero que ele que saber se é divisível, o segundo é por quanto dividir.
#Dê uma mensagem clara, como acima
num = int(input("Diga um número : "))
div = int(input("Diga por quanto voce quer saber se ele é divisível : "))
if num%div==0:
    print(f"O número {num} é dívisivel por {div}")
else:
    print(f"O número {num} tem resto {num%div} na divisão por {div}, isso quer dizer que {num}={num//div}*{div}+{num%div}")



#peça pro usuário 3 números
#printe na tela o maior deles

num1 = float(input("Diga o primeiro número : "))
num2 = float(input("Diga o segundo número : "))
num3 = float(input("Diga o terceiro número : "))


if num1 > num2 and num1 > num3:
    print(f"{num1} é o maior entre {num1},{num2},{num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} é o maior entre {num1},{num2},{num3}")
else:
    print(f"{num3} é o maior entre {num1},{num2},{num3}")

#peça pro usuário 3 números
#pergunte ao usuario se ele quer saber o maior ou o menor
#mostre na tela o maior ou o menor de acordo com a opção do usuario

num1 = float(input("Diga o primeiro número : "))
num2 = float(input("Diga o segundo número : "))
num3 = float(input("Diga o terceiro número : "))


maior_ou_menor = input("Voce quer achar o maior ou o menor ? ")

if maior_ou_menor == "maior":
    maior_numero = num3

    if num1 > num2 and num1 > num3:
        maior_numero = num1
    elif num2 > num1 and num2 > num3:
        maior_numero = num2

    print(f"{maior_numero} é o maior entre {num1},{num2},{num3}")

elif maior_ou_menor == "menor":
    if num1 < num2 and num1 < num3:
        print(f"{num1} é o menor entre {num1},{num2},{num3}")
    elif num2 < num1 and num2 < num3:
        print(f"{num2} é o menor entre {num1},{num2},{num3}")
    else:
        print(f"{num3} é o menor entre {num1},{num2},{num3}")
else:
    print("n tendi")

#receba dois numeros do usuario
#pergunte se ele quer saber a soma, a subtração, a divisao ou a multiplicação entre esses numeros
#de a resposta correta

resposta = input("Qual operação vc deseja fazer : +, -, / ou * ? ")
num1 = float(input("Diga o primeiro numero : "))
num2 = float(input("Diga o segundo numero : "))

if resposta == "+":
    print(f"A soma entre {num1} e {num2} é {num1+num2}")
elif resposta == "-":
    print(f"A subtração entre {num1} e {num2} é {num1-num2}")
elif resposta == "/":
    print(f"A divisao entre {num1} e {num2} é {num1/num2}")
elif resposta == "*":
    print(f"A multiplicação entre {num1} e {num2} é {num1*num2}")
else:
    print("n tendi")

    

#receba dois numeros do usuario e printe a subtração positiva (módulo ou valor absoluto)
a = float(input("diga um numero : "))
b = float(input("diga um numero : "))
'''
sub = a-b
if sub<0:
    sub*=-1
    #sub = sub*(-1)
print(sub)
'''
if a<b:
    aux = a
    a = b
    b = aux
print(a-b)