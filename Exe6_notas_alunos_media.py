notas_acima7 =[]
for i in range(1,11):
    notas = []
    print(f"aluno {i}")
    for i in range(1,5):
        nota = notas.append(float(input(f"Digite a {i}º: ")))
    media = sum(notas) / len(notas)
    if media >= 7:
        notas_acima7.append(media)
print(f"Obtivemos {len(notas_acima7)} alunos com nota maior ou igual a 7")
    


