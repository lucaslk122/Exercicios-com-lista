salarios_func = []
abonos =[]
while True:
    salario = int(input("Digite o salario do funcionario: "))
    if salario == 0:
        break
    else:
        salarios_func.append(salario)
    abono = abonos.append(salario*0.2)
minimo = 0
print("\nProjeção de Gastos com Abono")
print("="*50)
print("n\nSalario R$             Abono R$")
for i in range(len(salarios_func)):
    if abonos[i] < 100:
        print(f"{salarios_func[i]}                      100")
        abonos[i] = 100
        minimo += 1
    else:
        print(f"{salarios_func[i]}                    {abonos[i]}")
print(f"Foram processados {len(salarios_func)} colaboradores")
print(f"Total gasto com abono: R${sum(abonos)}")
print(f"Valor minimo pago a {minimo} funcionarios")
print(f"Maior valor de abono pago: R${max(abonos)}")