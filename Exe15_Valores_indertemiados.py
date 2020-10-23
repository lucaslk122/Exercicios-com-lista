valores = []
x = 0
while x != -1:
    x = float(input("Digite um numero, -1 para encerrar: "))
    valores.append(x)
print(f"Valores na ordem que foram digitados = {valores}")
print(f"Valores na ordem inversa = {valores[::-1]}")
print(f"Média do valores: {round((sum(valores) / len(valores)),2)}")