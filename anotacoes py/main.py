#print("Olá eu me chamo Danilo, tenho 26 anos balbalbalbalbalbalbab")
frase = "Olá eu me chamo Danilo, tenho 26 anos balbalbalbalbalbalbab"
#print(frase)
primeira_palavra = "Olá"
segunda_palavra = "Mundo"
print(primeira_palavra)
print(segunda_palavra)
print(primeira_palavra,segunda_palavra)
print(primeira_palavra+segunda_palavra)

sentenca = primeira_palavra + " " + segunda_palavra
#print("Este é o primeiro print da variavel sentenca : ",sentenca)
print("\n\n\n")
var1 = "Meu"
var2 = "nome"
var3 = "é"
var4 = "Danilo"

#sentenca = var1 + " " + var2 + " "+ var3 + " "+ var4
#print("Este é o segundo print da variavel sentenca : ",sentenca)

sentenca = "Meu"
print("Este é o primeiro print da variavel sentenca : ",sentenca)
sentenca = sentenca + " nome"
print("Este é o segundo print da variavel sentenca : ",sentenca)
sentenca = sentenca + " é"
print("Este é o terceiro print da variavel sentenca : ",sentenca)
sentenca = sentenca + " Luisa"
print("Este é o quarto print da variavel sentenca : ",sentenca)

#use essa estrutura para escrever "olá, sou tal, tenho tantos anos"
print("\n\n")
frase = "olá, "
print(frase)
frase = frase + "sou Luisa,"
print(frase)
frase = frase + " tenho 17 anos"
print(frase)

nome = input("Me diga seu nome : ")
idade = input("Me diga sua idade : ")
print(f"seu nome é {nome} e sua idade é {idade} anos")

#tipo de variável : string
#nome = "Danilo"
#print(type(nome))

#num1 = float(input("diga um numero : "))
#num2 = float(input("diga o segundo numero : "))
#print(type(num1),type(num2))
#soma = num1 + num2
#print(soma)
num1 = "17"
num2 = "19"
print(f"o tipo de num1 é {type(num1)}, o tipo de num2 é {type(num2)}")
soma = num1 + num2
print(f"Essa é a soma de strings {soma}")
num1 = int(num1)
num2 = int(num2)
soma = num1 + num2
print(f"o tipo de num1 é {type(num1)}, o tipo de num2 é {type(num2)}")
print(f"Essa é a soma de ints {soma}")

a = 1
b = "oi"
c = False
d = None
e = 2.0
#print(type(a))
#print(type(b))
#print(type(c))
#print(type(d))
#print(type(e))


#comparações entre inteiros : >, <, ==
a = 1
b = 2
print(a>b)
print(a<b)
print(a==b)
#operadores lógicos and : só retorna True quando ambas as sentenças lógicas forem verdadeiras 
c = 3
d = 4
print(c>d)
print(c<d)
print(c==d)
print("\n")
#print("Print das comparações", c<d and a<b)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

#operador lógico or : quando pelo menos uma das sentenças lógicas (comparação, etc) for verdadeira, retorna True
a=1
b=2
c=3
d=4
print(a>b or c>d)
print(a>b or c<d)
print(a<b or c>d)
print(a<b or c<d)

idade1 = input("me diga sua idade : ")
idade2 = input("me diga a outra idade : ")
print(f"comparando {idade1} > {idade2} : {idade1>idade2}")
print(f"comparando {idade1} < {idade2} : {idade1<idade2}")

#receba do usuário o valor de dois produtos e os compare

cerveja = int(input("me diga o preço da cerveja : "))
guaranazinho_po = int(input("me diga o preço do guaranazinho : "))
print(f"o guaranazinho é mais caro que a cerveja ? {guaranazinho_po>cerveja}")