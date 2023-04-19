

#receba um numero do usuario e verifique se ele é par ou ímpar
#se for par printe q o número é par, o mesmo para o ímpar
a = int(input("diga um numero : "))
if a%2==0:
    print(f"{a} é par")
else:
    print(f"{a} é ímpar")



#receba um numero do usuario e verifique se ele é multiplo de 3
#se for, printe que é multiplo, caso contrario diga que nao e mostre o resto
num = int(input("diga um numero : "))
resto = num%3
if resto==0:
    print(f"{num} é divisível por 3")
else:
    print(f"Não é multiplo! veja: {num} = {num//3}*3 + {resto}")



#peça ao usuario dois numeros, o principal e por quanto ele quer saber
#se é divisível
#printe a mensagem de resto se nao for divisivel
num = int(input("diga um numero : "))
div = int(input("Diga o segundo numero : "))
resto = num%div
if resto==0:
    print(f"{num} é divisível por 3")
else:
    print(f"Não é multiplo! veja: {num} = {num//div}*{div} + {resto}")



#peça 3 numeros de input do usuario
#printe na tela o maior deles
num1 = int(input("Diga o primeiro numero : "))
num2 = int(input("Diga o segundo numero : "))
num3 = int(input("Diga o terceiro numero : "))
if num1 > num2 and num1 > num3 :
    print(f"{num1} é o maior")
elif num2 > num1 and num2 > num3 :
    print(f"{num2} é o maior")
else:
    print(f"{num3} é o maior")
num1 = int(input("Diga o primeiro numero : "))
num2 = int(input("Diga o segundo numero : "))
num3 = int(input("Diga o terceiro numero : "))
maior = num1
if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
print(f"O maior é {maior}")



#peça 3 numeros para o usuario e pergunte a ele se ele quer encontrar
#o maior ou o menor dentre os digitados
#se ele quiser encontrar o maior, printe o maior, se o menor, print o menor

num1 = int(input("Diga o primeiro numero : "))
num2 = int(input("Diga o segundo numero : "))
num3 = int(input("Diga o terceiro numero : "))
resposta = input("Voce quer encontrar o maior ou o menor número ? ")
if resposta == "maior":
    if num1 > num2 and num1 > num3 :
        print(f"{num1} é o maior")
    elif num2 > num1 and num2 > num3 :
        print(f"{num2} é o maior")
    else:
        print(f"{num3} é o maior")
else:
    if num1 < num2 and num1 < num3 :
        print(f"{num1} é o menor")
    elif num2 < num1 and num2 < num3 :
        print(f"{num2} é o menor")
    else:
        print(f"{num3} é o menor")




#pergunte ao usuario se ele quer conhecer a sua calculadora
#se ele disser que sim, peça dois numeros e pergunte qual operação ele quer
#realizar: soma, subtração, divisao e multiplicação.
#printe o resultado



num1 = int(input("Diga o primeiro numero : "))
num2 = int(input("Diga o segundo numero : "))
resposta = input("vc quer conhecer minha calculadora ? ")

if resposta == "sim":
    operacao = input("o que vc quer: soma, subtração, divisão ou vezes")
    if operacao == "soma":
        print(f"{num1}+{num2}={num1+num2}")
    elif operacao == "subtração":
        print(f"{num1}-{num2}={num1-num2}")
    elif operacao == "divisão":
        print(f"{num1}/{num2}={num1/num2}")
    elif operacao == "vezes":
        print(f"{num1}*{num2}={num1*num2}")
    else:
        print("tendi nada")
else:
    print("babaca")



#defina uma variavel usuario
#defina uma variavel senha
#peça que o usuario digite seu usuario e senha
#sem ambos estiverem corretos printe : Acesso liberado!
#se somente o usuario estiver correto, diga que a senha está incorreta
#neste caso pergunte ao usuário se ele quer redefinir a senha
#em caso afirmativo, redefina a senha de acordo com o que ele digitar.

usuario = "mestre"
senha = "danilo"

usuario_digitado = input("Diga seu usuario : ")
senha_digitada = input("Diga sua senha : ")
if usuario == usuario_digitado and senha == senha_digitada:
    print("Acesso liberado")
elif  usuario_digitado == usuario:
    print(f"{usuario}, sua senha tá incorreta!")
    resposta = input("Deseja redefinir sua senha ?")
    if resposta == "sim":
        senha = input("Diga a nova senha : ")
        print("Senha alterada com sucesso")
    else:
        print("nao foi dessa vez troxa")
else:
    print("Acesso negado")