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

#rever
def ex4():
    letra = input("Digite uma letra, e descubra se ela é uma consoante ou uma vogal: \n")
    if letra == 'a' or 'e' or 'i' or 'o' or 'u':
        print("esta letra é uma vogal")
    else:
        print("esta letra é uma consoante")

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
