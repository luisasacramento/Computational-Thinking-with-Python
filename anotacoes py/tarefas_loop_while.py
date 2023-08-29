#Código de calculadora para forçar uma resposta q foi pre-definida (s/n)

resposta = input("Voce quer adquirir conhecimento ??? (s/n) ")
while not (resposta == "s" or resposta == "n"): #while resposta != "s" and resposta !="n"
    resposta = input("Mano tem que ser (s/n) ")
if resposta == "s":
    print("Parabens voce nao é boboca, bem vindo à calculadora!")
    while True:
        num1 = input("diga o primeiro número : ")
        num2 = input("diga o segundo número : ")
        while num1.isnumeric() == False or num2.isnumeric()==False:
            num1 = input("tem que ser numero seu animal : ")
            num2 = input("O segundo tb: ")
        num1 = int(num1)
        num2 = int(num2)
        opcao = input("Qual operação voce quer fazer? soma, subtração, divisão,\
         multiplicação ou sair?")
        while not (opcao == "soma" or opcao == "subtração" or opcao == "divisão"\
                   or opcao == "multiplicação" or opcao == "sair"):
            opcao = input("Qual operação voce quer fazer? soma, subtração, divisão,\
             multiplicação ou sair?")
        if opcao == "soma":
            resultado = num1 + num2
            print(f"O resultado da {opcao} entre {num1} e {num2} é {resultado}")
        elif opcao == "subtração":
            resultado = num1 - num2
            print(f"O resultado da {opcao} entre {num1} e {num2} é {resultado}")
        elif opcao == "divisão":
            resultado = num1 / num2
            print(f"O resultado da {opcao} entre {num1} e {num2} é {resultado}")
        elif opcao == "multiplicação":
            resultado = num1 * num2
            print(f"O resultado da {opcao} entre {num1} e {num2} é {resultado}")
        else:
            print("Tchau")
            break
else:
    print("seu boboca")


#Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido. 

nota = input("Diga sua nota : ")
if nota.isnumeric():
    if int(nota) >0 and int(nota)<10:
        print("digitou corretamente")
else:
    while True:
        nota= input("sua nota deve ser entre 0 e 10: ")
        if nota.isnumeric():
            nota_convertida = int(nota)
            if nota_convertida < 0 or nota_convertida > 10:
                continue
            else:
                print("digitou corretamente")
                break
        else:
            continue


while True:
    nota = input("sua nota deve ser entre 0 e 10: ")
    if nota.isnumeric():
        nota_convertida = int(nota)
        if nota_convertida < 0 or nota_convertida > 10:
            continue
        else:
            print("digitou corretamente")
            break
    else:
        continue


# Faça um programa que leia e valide as seguintes informações: 
# Nome: maior que 3 caracteres 
# Idade: entre 0 e 150
# Salário: maior que zero 
# Sexo: 'f' ou 'm'
# Estado Civil: 's', 'c', 'v', 'd'

nome = input("Diga seu nome : ")
while len(nome) < 3:
    nome = input("Diga seu nome : ")

idade = int(input("Diga sua idade : "))
while idade<0 and idade >150:
    idade = input("Diga sua idade : ")

salario = int(input("Diga seu salario : "))
while salario < 0:
    salario = int(input("Diga seu salario : "))

sexo = input("Diga seu sexo : ")
while not (sexo == "f" or sexo =="m"):
    sexo = input("Diga seu sexo : ")

estado_civil = input("Diga seu estado civil : ")
while not (estado_civil == "s" or estado_civil == "c" or \
           estado_civil == "v" or estado_civil == "d" ):
    estado_civil = input("Diga seu estado civil : ")



# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

#import matplotlib.pyplot as plt
pop_a = 80000
pop_b = 200000
t=0
a = [pop_a]
b = [pop_b]
tempo = [t]
while pop_a<pop_b:
    pop_a *= 1.03
    pop_b *= 1.015
    t+=1
    tempo.append(t)
    a.append(pop_a)
    b.append(pop_b)
print(t)

# plt.plot(tempo,a,"r",label = "pop A")
# plt.plot(tempo,b,"b",label = "pop B")
# plt.ylabel("Numero de habitantes")
# plt.xlabel("tempo")
# plt.legend()
# plt.title("Evoluçaõ temporal das populações")
# plt.grid()
# plt.show()

#pip install matplotlib



#Faça um programa que leia 5 números e informe a soma e a média dos números. 
i=0
soma=0
while i<5:
    num = int(input(f"Diga o {i}º numero : "))
    soma+=num
    i+=1
media = soma/i
print(f"A media é {media} e a soma é {soma}")

num1 = int(input("Diga um numero : "))
num2 = int(input("Diga um numero : "))

if num1 <num2:
    while num1<num2:
        print(num1)
        num1+=1
else:
    while num2<num1:
        print(num2)
        num2+=1



# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. 
a=1
b=1
i=0
qtd = int(input("qts numeros de fibonacci vc quer saber ? "))
print(a)
print(b)
while i< qtd:
    c=a+b
    a=b
    b=c
    i+=1
    print(c)
