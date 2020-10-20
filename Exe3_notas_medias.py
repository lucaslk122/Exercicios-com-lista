lista = []
for i in range(4):
    notas = float(input(f"Digite a {i}º nota: "))
    lista.append(notas)
media = sum(lista) / len(lista)
print("Média das notas: ",media)