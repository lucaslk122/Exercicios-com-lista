valores = []
while True:
    x = float(input("Digite um numero, -1 para encerrar: "))
    if x != -1:
        valores.append(x)
    else:
        break
print(f"Foram lidos {len(valores)} valores")
print(f"Valores na ordem que foram digitados = {valores}")
print(f"Valores na ordem inversa = {valores[::-1]}")
print(f"Média do valores: {round((sum(valores) / len(valores)),2)}")