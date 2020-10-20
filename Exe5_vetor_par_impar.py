lista = []
pares = []
impar = []
for i in range(20):
    lista.append(int(input("Digite um numero: ")))
#print(lista)
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impar.append(i)
print(f"Lista = {lista}")
print(f"Pares = {pares}")
print(f"impar = {impar}")