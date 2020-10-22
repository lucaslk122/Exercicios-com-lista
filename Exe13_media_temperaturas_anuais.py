temperatura = []
meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media_acima = {}
for i in range(len(meses)):
    temperatura.append(float(input(f"Digite a temperatura do mês {meses[i]}: ")))
media = round(sum(temperatura) / len(temperatura),2)
c = 0
while c < len(meses):
    if temperatura[c] > media:
        media_acima.update({meses[c]:temperatura[c]})
    c += 1
print(f"Média das temperaturas: {media}")
print(f"Meses com a temperatura acima da média: {media_acima}")
