print("""Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
""")
windows,unix,linux,netware,macOS,outro = 0,0,0,0,0,0
while True:
    opção = int(input("Digite a opção: "))
    if opção == 1:
        windows += 1
    elif opção == 2:
        unix += 1
    elif opção == 3:
        linux += 1
    elif opção == 4:
        netware += 1
    elif opção == 5:
        macOS += 1
    elif opção == 6:
        outro += 1
    elif opção > 6:
        print("Opção invalida, não será computado:")
    else:
        break
total_votos = windows + unix + linux + netware + macOS + outro
votos_operacioansi = {}
votos =[]
sistemas_operacionais = ["windows","unix","linux","netware","macOS","outro"]
for i in len(total_votos):
    votos.append(sistemas_operacionais[i])
c = 0
while c < len(sistemas_operacionais):
    votos_operacioansi.update({sistemas_operacionais[c]:votos[c]})
    c += 1
print(votos)

"""
print("Sistema operacional            Votos            %")
print("-"*50)
print(f"Windows Server:                 {windows}            {round(((windows*100) / total_votos),2)}")
print(f"Unix:                           {unix}            {round(((unix*100) / total_votos),2)}")        
print(f"Linux:                          {linux}              {round(((linux*100) / total_votos),2)}")
print(f"Netware:                        {netware}               {round(((netware*100) / total_votos),2)}")
print(f"Mac OS:                         {macOS}           {round(((macOS*100) / total_votos),2)}")
print(f"Outro:                          {outro}            {round(((outro*100) / total_votos),2)}")
print("-"*50)
print(f"Total :                         {total_votos}")
"""