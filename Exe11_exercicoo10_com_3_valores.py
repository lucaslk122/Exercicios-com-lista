lista1 =[]
lista2 =[]
lista3 = []
lista4 = []
for i in range(10):
    lista1.append(int(input("Digite um valor para a primeira lista: ")))
    lista2.append(int(input("Digite um valor para a segunda lista: ")))
    lista3.append(int(input("Digite um valor para a terceira lista: ")))
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print(lista1)
print(lista2)
print(lista3)
print(lista4)