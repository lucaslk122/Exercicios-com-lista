altura =[]
idade = []
for i in range(1,6):
    idade.append(int(input(f"Digite a idade da {i}º da primeira pessoa: ")))
    altura.append(float(input(f"Digite a altura da {i}º da primeira pessoa: ")))

print("lista da idade em ordem normal: ",idade)
print("Lista das idades invertida: ",idade[::-1])
print("lista da altura em ordem normal: ",altura)
print("Lista das altura invertida: ",altura[::-1])