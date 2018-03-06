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
