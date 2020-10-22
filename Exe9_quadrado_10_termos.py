valores =[]
valores_quadrado =[]
for i in range(10):
    valores.append(int(input("Digite um numero inteiro: ")))
for i in valores:
    valores_quadrado.append(i**2)
print("Valores da lista ao quadrado: ",valores_quadrado)
print("Soma dos quadrados: ",sum(valores_quadrado))