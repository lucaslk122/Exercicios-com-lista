nome = True
salto = []
while nome != "":
    nome = input("Nome do atletra: ")
    if nome == "":
        break
    else:
        for i in range(1,6):
            x = float(input(f"{i}º salto: "))
            salto.append(x)
    print(f"Melhor salto: {max(salto)}")
    print(f"Pior salto: {min(salto)}")
    media = sum(salto) / len(salto)
    print(f"Média dos saltos: {round(media,2)}m")
    print(f"""Resultado final:
    {nome} : {round(media,2)}m""")