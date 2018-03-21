dic = {}
dic1= {}
final = []
media = 0
for c in range (0,4):
    nome = input("digite o nome:\n")
    sexo = input("digite o sexo (F - feminino) ou (M - masculino):")
    idade = int(input("dgite a idade:"))
    media += idade
    sexo = sexo.lower()
    if sexo == 'm':
        dic[nome] = idade
    elif sexo == 'f':
        dic1[nome] = idade
for m in dic1:
    if dic1[m] < 20:
       final.append(m) 
media = media / 4

print("mulheres com idade < 20 é: {}".format(len(final)))
print("o homem mais velho é: {}".format(max(dic, key=dic.get)))
print("a idade é: {}".format(dic[max(dic, key=dic.get)]))
print("media de idade do grupo é: {:.0f}".format(media))

