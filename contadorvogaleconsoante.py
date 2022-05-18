vogal = ["a" , "e" , "i" , "o" , "u"]
a = []
vogais = 0
conso = 0
for x in range (0,10):
    letra = (input())
    a.append(x)
    if letra in vogal:
        vogais = vogais + 1
    else:
        conso = conso + 1

print(vogais)
print(conso)