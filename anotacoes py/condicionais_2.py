#em uma vendinha maçãs custam R$00,50 a unidade
#se a qtd for maior do que 20 ou o cliente tiver cadastro,
#cada uma passa a custar 0,35.

#faça duas perguntas ao usuario, se ele tem cadastro e a qtd de maçãs
#que ele está comprando. Calcule quanto ele gastou.

cadastro = input("Voce tem cadastro ? (s/n) ")
qtd = int(input("Qts maças vc comprou ? "))

if qtd > 20 or cadastro == "s":
    preco = 0.35
    total = qtd*preco
    print(f"Voce pagará R${total} por {qtd} maças")
else:
    preco = 0.5
    total = qtd*preco
    print(f"Voce pagará R${total} por {qtd} maças")


cadastro = input("Voce tem cadastro ? (s/n) ")
preco = 0.5
if cadastro =="s":
    preco = 0.35
    qtd = int(input("quantas maças vc vai comprar ?"))
else:
    qtd = int(input("quantas maças vc vai comprar ?"))
    if qtd > 20:
        preco = 0.35


total = preco*qtd
print(f"o total foi de R${total}")


qntd = int(input("Quantas maçãs você irá comprar:"))
cdt = input("Você possui cadastro na loja? (se sim digite 'sim', caso contrário digite 'não'):")
if qntd>20 or cdt == "sim":
    print(f"Você ganhou um desconto de R$00,15 em cada maçã, portanto o preço total das maçãs ficou = {qntd * 0.35}")
if qntd<20 or cdt == "não":
    print(f"O preço total das maçãs ficou: {qntd * 0.50}")
print("Obrigado por comprar aqui e na próxima compre mais!!")





#defina duas varias: nome de usuario e senha no seu codigo
#depois disso peça de input o usuario e senha
#se ambos estiverem corretos de uma mensagem de acesso liberado
#se o nome estiver certo mas a senha errada, pergunte se quer redefinir senha
#se ele quiser, redefina a variavel senha
#se desde o inicio ele errar tudo printe hacker

user = "celtinha_preto_zica_demais"
senha = "arcondicionado"

username = input("Diga o nome de usuario : ")
password = input("Diga sua senha : ")
if user == username and senha == password:
    print("voa celtinha")
elif user == username and senha != password:
    redefinir =  input("quer redefinir a senha ? (S/N)")
    if redefinir == "S":
        senha = input("diga a nova senha : ")
    else:
        print("tchau")
else:
    print("n roba meu celta porra")

#Outro jeito

nome = "Pedro Henrique"
senha = 2001

usuario = input("Digite seu nome:")
passw = input("Digite sua senha:")
if usuario == nome:
    if passw == senha:
        print("Acesso liberado")
    else:
        red = input("Deseja redefinir senha?")
        if red == "sim":
            reds = input("Digite a nova senha:")
            senha = reds
else:
    print("hacker")



#de 4 opções pro usuario, 1- cadastrar, 2- ver estoque, 3- promoções, 4- sair
#para cada uma delas faça um print adequado

print("vc tem 4 opções: 1- cadastrar, 2- ver estoque, 3- promoções, 4- sair" )
resposta = int(input("Diga sua opção : "))

if resposta == 1:
    print("cadastro")
elif resposta == 2:
    print("10 caixas")
elif resposta == 3:
    print("promoção de queijo")
else:
    print("sair")




#calculadora de soma e subtração

resposta = input("Voce deseja conhecer a minha calculadora ? ")

if resposta == "sim":
    resposta_2 = input("Voce quer saber a soma (+) ou subtração (-)? ")
    if resposta_2 == "+":
        num1 = float(input("diga o primeiro número : "))
        num2 = float(input("diga o segundo número : "))
        print(f"a soma é {num1+num2}")
    else:
        num1 = float(input("diga o primeiro número : "))
        num2 = float(input("diga o segundo número : "))
        print(f"a subtração é {num1-num2}")
else:
    print("FODASE")
