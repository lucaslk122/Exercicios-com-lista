lista = []
consoantes = 0
for i in range(10):
    lista.append(input("Digite uma letra: ").lower())
    char = lista[i]
    if char not in ('a','e','i','o','u'):
        consoantes += 1
print(consoantes)
