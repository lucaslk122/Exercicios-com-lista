perguntas = []
print("Para cada pergunta, responda s para sim e n para não")
perguntas.append(input("Telefonou para a vítima?: ").lower())
perguntas.append(input("Esteve no local do crime?: ").lower())
perguntas.append(input("Mora perto da vítima?: ").lower())
perguntas.append(input("Já trabalhou com a vítima?: ").lower())
perguntas.append(input("Devia para a vítima?: ").lower())
if perguntas.count("s") == 2:
    print("Suspeita")
elif perguntas.count("s") == 3 or perguntas.count(1) == 4:
    print("Cúmplice")
elif perguntas.count("s") == 5:
    print("Assassino")
else:
    print("Inocente")
