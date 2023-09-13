frase = "A aranha arranha a rã A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
frase = frase.replace(".", '')
frase = frase.lower()
print(frase)
print("a" == "A")
frase = frase.split(" ")
print(frase)


dict = {}
for palavra in frase:
    if palavra not in dict.keys():
        dict[palavra] = 0
print(dict)

for palavra in frase:
    if palavra in dict.keys():
        dict[palavra] +=1
print(dict)

#melhor jeito de fazer
dict = {}
for palavra in frase:
    if palavra not in dict.keys():
        dict[palavra] = 1
    else:
        dict[palavra] += 1
print(dict)
