valores = []
while True:
    x = float(input("Digite um numero, -1 para encerrar: "))
    if x != -1:
        valores.append(x)
    else:
        break
media = sum(valores) / len(valores)
print(f"Foram lidos {len(valores)} valores")
print(f"Valores na ordem que foram digitados = {valores}")
print(f"Valores na ordem inversa = {valores[::-1]}")
print(f"Soma dos valores = {round(sum(valores),2)}")
print(f"Média do valores: {round(media,2)}")
c = 0
acima_media =[]
abaixo_media =[]
while c < len(valores):
    if valores[c] > media:
        acima_media.append(valores[c])
    else:
        abaixo_media.append(valores[c])
    c += 1
print(f"Valores acima da média = {acima_media}")
print(f"Valores abaixo da média = {abaixo_media}")