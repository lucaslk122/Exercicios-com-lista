lista1 =[]
lista2 =[]
lista = []

for i in range(10):
    lista1.append(int(input("Digite um valor para a primeira lista: ")))
    lista2.append(int(input("Digite um valor para a segunda lista: ")))
    lista.append(lista1[i])
    lista.append(lista2[i])

print(lista1)
print(lista2)
print(lista)