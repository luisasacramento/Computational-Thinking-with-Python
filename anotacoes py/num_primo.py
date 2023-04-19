#Checkpoint 1 - 10

#numero primo divisivel por um e por ele mesmo 
#7%2=1 ---- significa sete por cento 2, o dois cabe tres vezes dentro do sete e sobra 1. 

#  17
#  17%2 = 1 
#  17%3 = 2 
#  17%4 = 1 
#  | 
#  | 
#  | 
#  17%14 = 3 
#  17%15 = 2 
#  17%16 = 1



#Formas de verificar se um numero é primo

num = 17 
i = 2 #começa a checar a partir de 2

while i <num: 
    print(f"{num}%{i} = {num%i}") 
    if num%i == 0: 
        print(f"{num} não é primo pois é divisivel por {i}") 
        break 
    elif i == num-1: print('é primo :)') 
i+=1

#Outro jeito
num = 45 
qte_divs = 0 
i=1 
while i < num: 
    if num%i == 0: 
        qte_divs+=1 
        i+=1 
        if qte_divs == 2: print(f"{num} é primo") 
        else: print(f"{num} tem {qte_divs} divisores") 

#Outro 
num = int((input("Diga um numero ")))
qtd_divs = 0
i=2
while i<num:
    if num%i==0:
        qtd_divs+=1
        print(f"{num} não é primo")
        break
    elif i==num-1:
        print(f"{num} é primo")
        i+=1

#numeros de 0 ate 100 que são primos
num = 0 
qtd_divs = 0 
while num <100: 
    #num+=1 
    i=2 
    while i < num: 
        print(f"{num}%{i} = {num%i}") 
        if num%i ==0: 
            qtd_divs+=1 
            break 
        elif i >= num/2: 
            print(f"{num} é primo") 
            break 
        i+=1 
        num+=1 

#todos numeros primos da sequencia de fibonacci até 1000 

a=1 
b=1 
qtd=0 
while qtd <100:
    c=a+b 
    a=b 
    b=c 
    qtd+=1 
    print(c)
i=0
while i < c:
    print(f"{c}%{i} = {c % i}")
    if c % i == 0:
        qtd += 1
        break
    elif i >= c / 2:
        print(f"{c} é primo")
        break
    i += 1
c += 1