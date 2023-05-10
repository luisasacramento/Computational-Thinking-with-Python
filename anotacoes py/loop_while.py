

'''
soma = 0

while i <= 10:
    print(i)
    soma += i
    i+=1
    print(f"o valor da soma é {soma}")
'''

'''
i=0
num = int(input("diga um numero(0 para sair) : "))

while num !=0:
    num = int(input("Diga um numero: "))
    if num%2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
    i+= 1
print(f"voce testou {i} numeros")
'''


'''
a = (input("Voce quer ver as vogais?"))

if a == "sim":   
    letra = (input("diga uma letra(sair para deixar de executar) : "))
    while letra != "sair":

         if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            print(f"{letra} é vogal")
         else:
            print(f"{letra} é consoante")
            letra = (input("Diga uma letra :"))
else:
   print("bobo")
   
'''

'''

senha = "1234"
login = "Danilo"

password = input("Diga seu usuario: ")
password = input("Diga sua senha: ")

while senha!= password or login != user:
    print("Acesso Negado")
    user = input("Diga seu usuario: ")
    password = input("Diga sua senha: ")
print("Acesso concedido ")

'''
senha = "1234"
login = "Danilo"
i = 0

password = input("Diga seu usuario: ")
password = input("Diga sua senha: ")

while (senha!= password or login != user) and i<=2:
    print("Acesso Negado")
    user = input("Diga seu usuario: ")
    password = input("Diga sua senha: ")
    i+=1
if i ==2:
   print("Acesso concedido ")