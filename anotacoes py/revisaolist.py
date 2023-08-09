'''
lista = ["Danilo", "allen", "Cordeiro", "israel", "Francisco"]

for i in range(len(lista)):
    print(f"o {lista[i]} está no indice {i}")

senha = "12345"
senha_usuario = input("Diga sus senha: ")
tentativas = 1
while senha_usuario != senha and tentativas<3:
    print("errooou")
    senha_usuario = input("Diga sua senha: ")
    tentativas +=1 
if senha == senha_usuario:
    print("acesso liberado")
else:
    print("sai hacker")


for i in range(3):
    senha_usuario: input("Diga sua senha: ")
    if senha == senha_usuario:
        print("acesso liberado")

'''

lista = ["Danilo", "allen", "Cordeiro", "israel", "Francisco"]

if "Danilo" in lista:
    print(True)
    print(lista.index("Danilo"))


for nome in lista:
    if nome == "Danilo":
        print("Encontrei")

i=0
for nome in lista:
    if nome == "Danilo":
        print("Encontrei no {i}")
    i+=1



#imagem é um matriz numerica
