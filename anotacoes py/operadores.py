a = 1
b = 2.0
c = "danilo"
d = True
e = False
f = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#operadores lógicos:  <,> , ==, !=, <=, >=, or, and, not, in, is

comp1 = a>b
print(f"a comparação {a}>{b} resulta em {comp1}")
comp2 = a<b
print(f"a comparação {a}<{b} resulta em {comp2}")

res_and = a>b and b>a

a = 2
b = 3

res_and = a>b and b>a
print(f"a comp entre {a>b} and {b>a} é {res_and}")
print(f"a comp entre {a<b} and {b>a} é {a<b and b>a}")
print(f"a comp entre {a<b} and {b<a} é {a<b and b<a}")
print(f"a comp entre {a>b} and {b<a} é {a>b and b<a}")


comp1 = 1>2 or 5>4
comp2 = 1<2 or 5>4
comp3 = 1<2 or 5<4
comp4 = 1>2 or 5<4
print(f"comp1 é {comp1}")
print(f"comp2 é {comp2}")
print(f"comp3 é {comp3}")
print(f"comp4 é {comp4}")


salario = float(input("diga seu salario : "))
idade = float(input("diga sua idade : "))
if salario>10000 and idade> 70:
    print("velho da lancha")
elif(salario<10000 and salario>8000):
    print("aspirante a burgues")
else:
    print("pobre")


#Peca uma letra para o usuario, 
# se for vogal printe q é vogal, se for consoante printe q é consoante

letra = input("digite uma letra : ")
if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("vogal")
else:
    print("consoante")

#Outro jeio 

letra = input("digite uma letra : ")
if letra==("a" or "e" or "i" or "o" or "u"):
    print("vogal")
else:
    print("consoante")


if letra=="a":
     print("vogal")
elif letra=="e":
    print("vogal")
elif letra=="i":
     print("vogal")
elif letra=="o":
    print("vogal")
elif letra=="u":
     print("vogal")
else:
     print("consoante")





#peça as notas q o usuario teve e calcule a média
#menor que 4 reprovou
#menor que 6 está de exame 
#acima disso está aprovado

nota_1 = float(input("diga a primeira nota : "))
nota_2 = float(input("diga a segunda nota : "))

media = (nota_1+nota_2)/2

if media<4:
    print("reprovou haha")
elif media <6:
    print("exame")
else:
    print("passou")



#Peca 4 numeros para o usuario e verifica qual deles é o maior de todos 

a = input('digite o primeiro numero: ')
b = input('digite o segundo numero: ')
c = input('digite o terceiro numero: ')
d = input('digite o quarto numero: ')

resposta = input("voce quer ver qual o maior numero? ")

if resposta == "sim":
    if a > b and a > c and a > d:
        print(f"{a} é o maior numero")
    elif b > a and b > c and b > d:
        print(f"{b} é o maior numero")
    elif c > a and c > b and c > d:
        print(f"{c} é o maior")
    else:
        print(f"{d} é o maior")

#melhor resposta

    if a > b and a > c and a > d:
        print(f"{a} é o maior numero")
    elif b > c  and b > d:
        print(f"{b} é o maior numero")
    elif c > d:
        print(f"{c} é o maior")
    else:
        print(f"{d} é o maior")


#Outro jeito 
a = input('digite o primeiro numero: ')
b = input('digite o segundo numero: ')
c = input('digite o terceiro numero: ')
d = input('digite o quarto numero: ')

resposta = input("voce quer ver qual o maior ou o menor numero? ")

if resposta == "maior":
    if a > b and a > c and a > d:
        print(f"{a} é o maior numero")
    elif b > a and b > c and b > d:
        print(f"{b} é o maior numero")
    elif c > a and c > b and c > d:
        print(f"{c} é o maior")
    else:
        print(f"{d} é o maior")
else:
    if a < b and a < c and a < d:
        print(f"{a} é o menor numero")
    elif b < a and b < c and b < d:
        print(f"{b} é o menor numero")
    elif c < a and c < b and c < d:
        print(f"{c} é o menor")
    else:
        print(f"{d} é o menor")


#outro jeito
a = input('digite o primeiro numero: ')
b = input('digite o segundo numero: ')
c = input('digite o terceiro numero: ')
d = input('digite o quarto numero: ')

menor_de_todos = a
if b <menor_de_todos:
    menor_de_todos = b
if c < menor_de_todos:
     menor_de_todos = c
if d < menor_de_todos:
     menor_de_todos = d
print(f"{menor_de_todos} é o menor")

