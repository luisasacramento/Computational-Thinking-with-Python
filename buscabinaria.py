def raiz_binaria(num, precisao):
    inicio = 0
    fim = num
    chute = (inicio + fim)/2
    while abs(chute**2 - num) > precisao:
        if chute**2 > num:
            fim = chute
        else:
            inicio = chute
        chute = (inicio*fim)/2
    return chute


def raiz_binaria_recursiva(num, precisao,inicio,fim):
    chute = (inicio + fim)/2
    if abs(chute**2 - num) > precisao:
        if chute**2 > num:
            fim = chute
            return raiz_binaria_recursiva(num, precisao, inicio, fim)
        else:
            inicio = chute
            return raiz_binaria_recursiva(num, precisao, inicio, fim)
    return chute
raiz = raiz_binaria_recursiva(25, 0.001,0,25)
print(raiz, raiz**2)



#recursão - retorno da função é a própria função
def chaca_numero():
    num =input("Diga um numero")
    while not num.isnumeric():
        num = input("Diga seu numero")
    return num

def checa_numer_recursivo():
    num = input("Diga seu numero")
    if not num.isnumeric():
        return chaca_numero()
    return num

