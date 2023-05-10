
print('impares')
for i in range(1,100,2):
    print(i)
print('pares')
for i in range(0,100,2):
    print(i)


for i in range(100):
    if i%2==0:
        print(f"{i} é par")


#tabuada

numero = int(input("Diga um numero e mostro a tabuada dele"))

for i in range(11):
    multi = numero * i
    print(multi)

#tabuada de todos os numeros
for num in range(1,11):
    print(f"A tabuada do {num} é : ")
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")


#pedir 10 números para o úsuarios e calcular a soma e média deles
soma = 0
maximo = 0
for i in range (maximo):
    soma+=int(input('Diga um numero: '))
media = soma/maximo
print(soma)
print(media)



#meu jeito
usuario = 'luisa'
senha = 00000
usuarioinpt = input("diga seu usuario:")
senhainpt = input("diga sua senha:")

if usuarioinpt != usuario and senhainpt != senha:
    for i in range(4):
        print('Errou tente de novo')
        input("diga seu usuario:")
        input("diga sua senha:")


#professor
nome = 'dan'
senha='123'
for i in range(3):
    password = input("Diga sua senha:")
    user = input("diga seu nome:")
    if nome == user and senha == password:
        print("acesso liberado")
        break
    print(f"burro vc tem mais {2-i} tentativas")