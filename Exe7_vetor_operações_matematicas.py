import functools 
import operator 
valores= []
valores_multiplicação =[]
for i in range(5):
    num = valores.append(int(input("Digite um numero: ")))
print(f"Valores = {valores}")
print(f"Soma = {sum(valores)}")
print (f"Produto = {functools.reduce(operator.mul,valores)}") 
