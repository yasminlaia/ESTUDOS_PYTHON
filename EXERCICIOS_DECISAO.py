def ex1():
    n1 = int(input("digite um numero inteiro: \n"))
    n2 = int(input("digite outro numero inteiro: \n"))

    if n1 > n2:
        print("o número {} é maior".format(n1))
    else:
        print("o numero {} maior".format(n2))
        
def ex2():
    valor = int(input("digite um numero, podendo ser positivo ou negativo: \n"))
    if valor > 0:
        print("o numero {} é positivo".format(valor))
    else:
        print("o numero {} é negativo".format(valor))

def ex3():
    sexo = input("digite as letras F, M para informar o sexo:")
    if sexo == 'M':
        print("Masculino")
    elif sexo == 'F':
            print("Feminino")
    else:
        print("Sexo inválido. Digite M para masculino ou F para feminino")


def ex4():
    letra = input("Digite uma letra, e descubra se ela é uma consoante ou uma vogal: \n")
    if letra == 'a' or letra =='e' or letra == 'i' or letra =='o' or letra == 'u':
        print("esta letra é uma vogal")
    else:
        print("esta letra é uma consoante")
def ex4():
    teste = 'aeiou'
    while True :
        letra = input("Digite uma letra, e descubra se ela é uma consoante ou uma vogal: \n")
        if letra in teste:
            print("esta letra é uma vogal")
        else:
            print("esta letra é uma consoante")
ex4()

def ex5():
    n1 = float(input("digite a primeira nota: \n"))
    n2 = float(input("digite a segunda nota: \n"))
    media = (n1 + n2)/2

    if media >=7:
        print("Aluno aprovado")
        if media == 10:
            print("Aprovado com distinção")
    else:
        print("Aluno reprovado")
        
def ex6():
    n1 = int(input("digite o primeiro numero:\n"))
    n2 = int(input("digite o segundo numero:\n"))
    n3 = int(input("digite o terceiro numero:\n"))
    
    if n1>n2 and n1>n3:
        print("o primeiro numero é maior")
    elif n2>n1 and n2>n3:
        print("o segundo numero é maior")
    else:
        print("o terceiro numero é maior")
        
def ex7():
    n1 = int(input("digite o primeiro numero:\n"))
    n2 = int(input("digite o segundo numero:\n"))
    n3 = int(input("digite o terceiro numero:\n"))

    if n1>n2 and n1>n3:
        print("o primeiro numero é maior")
    else:
        print("o primeiro numero é menor")
    if n2>n1 and n2>n3:
        print("o segundo numero é maior")
    else:
        print("o segundo numero é menor")
    if n3>n1 and n3>n2:
        print("o terceiro numero é maior")
    else:
        print("o terceiro numero é menor")
        
def ex8():
    
p1 = float(input("digite o preço do primeiro produto em reais:\n"))
p2 = float(input("digite o preço do segundo produto em reais:\n"))
p3 = float(input("digite o preço do terceiro produto em reais:\n"))

if p1<p2 and p1<p3:
    print("o primeiro produto com preço de R$ {} é mais barato.".format(p1))
elif p2<p1 and p2<p3:
    print("o segundo produto com preço de R$ {} é mais barato.".format(p2))
elif p3<p1 and p3<p2:
    print("o terceiro produto com preço de R$ {} é mais barato.".format(p3))

def ex9():
    numeros = []
    menores = []
    cont = 0
    n1 = int(input("digite o primeiro numero:"))
    n2 = int(input("digite o segundo numero:"))
    n3 = int(input("digite o terceiro numero:"))
    numeros.append(n1)
    numeros.append(n2)
    numeros.append(n3)
    while numeros is not None :
        if len(numeros) > 0  :            
            menores.append(max(numeros))
            numeros.remove(max(numeros))
        elif len(numeros) == 0:
            break
    print(menores) 
    
def ex10():
    turno = input("digite o periodo que estuda: M-matutino V-Vespertino ou N-Noturno")

    turno = turno.lower()
    if turno == 'm':
        print('Bom  dia')
    elif turno == 'v':
        print("Boa tarde")
    elif turno == 'n':
        print("Boa noite")
    else:
        print("Valor invalido")
        
    
def ex11():
    salario = float(input("digite o salario do colaborador:"))
    porcentagem = '0' 
    if salario <=280:
        aumento = salario*0.20
        porcentagem = '20%'
    elif salario > 280 and salario <=700 :
        aumento = salario*0.15
        porcentagem = '15%'
    elif salario > 700 and salario <=1500:
        aumento = salario * 0.10
        porcentagem = '10%'
    elif salario > 1500:
        aumento = salario * 0.05
        porcentagem = '5%'
    
    print("o salario sem reajuste é: {} reais".format(salario))
    print("o valor do aumento é: {} reais".format(aumento))
    print("o salario com aumento é: {} reais".format(salario+aumento))
    print("porcentagem do aumento é: {} %".format(porcentagem))
    
def ex13():
    semana = int(input("Digite o dia da semana que deseja: \n1-Domingo \n2-Segunda \n3-Terça \n4-Quarta \n5-Quinta \n6-Sexta \n7-Sábado \n"))

    if semana == 1:
        print("O dia da semana é Domingo")
    elif semana == 2:
        print("O dia da semana é Segunda")
    elif semana == 3:
        print("O dia da semana é Terça")
    elif semana == 4:
        print("O dia da semana é Quarta")
    elif semana == 5:
        print("O dia da semana é Quinta")
    elif semana == 6:
        print("O dia da semana é Sexta")
    elif semana == 7:
        print("O dia da semana é Sábado")
    else:
        print("Valor inválido. Digite de 1 a 7")
        
    def ex14():
    n=0
    while n<5:
        n+=1
        nome = input("Nome completo do aluno:\n")
        disciplina = input("Disciplina:\n")
        n1 = float(input("Nota da primeira prova:\n"))
        n2 = float(input("Nota da segunda prova:\n"))
        media = (n1 + n2) / 2

        if n1 >10 or n2 > 10:
            print("As notas devem ser entre 0 e 10")
        elif media >=9 and media <=10:
            print("ALUNO APROVADO")
            print("CONCEITO A")
            print("Média total: {}".format(media))
        elif media >=7.5 and media <=9:
            print("ALUNO APROVADO")
            print("CONCEITO B")
            print("Média total: {}".format(media))
        elif media >=6 and media <=7.5:
            print("ALUNO APROVADO")
            print("CONCEITO C")
            print("Média total: {}".format(media))
            
        elif media >=4 and media <= 6:
            print("ALUNO REPROVADO")
            print("CONCEITO D")
            print("Média total: {}".format(media))
            
        elif media == 0 and media <=4:
            print("ALUNO REPROVADO")
            print("CONCEITO E")
            print("Média total: {}".format(media))


        

