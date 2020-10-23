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
print("Sistema operacional            Votos            %")
print("-"*50)
total_votos = windows + unix + linux + netware + macOS + outro
votos_servidores= [windows,unix,linux,netware,macOS,outro]
print(f"Windows Server:                 {windows}            {round(((windows*100) / total_votos),2)}")
print(f"Unix:                           {unix}            {round(((unix*100) / total_votos),2)}")        
print(f"Linux:                          {linux}              {round(((linux*100) / total_votos),2)}")
print(f"Netware:                        {netware}               {round(((netware*100) / total_votos),2)}")
print(f"Mac OS:                         {macOS}           {round(((macOS*100) / total_votos),2)}")
print(f"Outro:                          {outro}            {round(((outro*100) / total_votos),2)}")
print("-"*50)
print(f"Total :                         {total_votos}")
