modelos_carros = []
combustivel = []
print("Deixe o espaço do nome do carro em branco para parar a leitura de dados")
while True:
    carro = input("Nome do carro: ")
    if carro != "":
        modelos_carros.append(carro)
    else:
        break
combustivel_carro = {}
for i in range(len(modelos_carros)):
    combustivel.append(float(input(f"{modelos_carros[i]} - Km por litro: ")))
c = 0
while c < len(modelos_carros):
    combustivel_carro.update({modelos_carros[c]:combustivel[c]})
    c += 1
print("Relatório final")
for i in range(len(combustivel_carro)):
    print(i+1, " - ", modelos_carros[i], " - ", combustivel_carro[i], " - ", round(1000 / combustivel_carro[i], 2), " - R$", round(1000 / combustivel_carro[i] * 2.25, 2))
indice_menor_consumo = combustivel_carro.index(max(combustivel_carro))
print("O menor consumo é o do ", modelos_carros[indice_menor_consumo])