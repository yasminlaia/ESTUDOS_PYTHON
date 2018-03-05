def ex1():
    print("Alo mundo")

def ex2():
    n = input("digite um numero:\n")
    print("o numero informado foi: {}".format(n))

def ex3():
    n1 = int(input("digite um numero:\n"))
    n2 = int(input("digite outro numero:\n"))
    print("a soma dos dois numeros é: {}".format(n1+n2))

def ex4():
    n1 = float
    (input("digite a primeira nota:\n"))
    n2 = float(input("digite a segunda nota:\n"))
    n3 = float(input("digite a terceira nota:\n"))
    n4 = float(input("digite a quarta nota:\n"))
    print("a media total é de:{}".format((n1+n2+n3+n4)/4))

def ex5():
    qtde_metros = float(input("digite a quantidade de metros que deseja converter em centimetros:\n"))
    print("a quantidade de centimetros é: {} cm".format(qtde_metros*100)) 

def ex6():
    pi = 3.14
    raio = float(input("informe o raio do circulo:\n"))
    print("a area do circulo é: {}".format(pi*raio**2))

def ex7():
    lado_quadrado = 5
    print("a area do quadrado é de: {}".format(lado_quadrado**2))
    print("o dobro da area do quadrado é de: {}".format((lado_quadrado**2)*2))

def ex8():
    valor_hora = int(input("digite quanto vc ganha por hora:\n"))
    qtde_horas = int(input("digite o numero de horas trabalhadas (mês):\n"))
    print("salario mensal é: {}".format(valor_hora*qtde_horas))

def ex9():
    f = float(input("digite a temperatura farenheit para conversao em graus celsius:\n"))
    print("a temperatura em graus celsius é de: {} graus".format
          (5*(f-32)/9))

def ex10():
    c = float(input("digite a temperatura celsius para conversao em farenheit:\n"))
    f = (c*1.8) + 32
    print("a temperatura em fahrenheit é de: {} graus".format(f))

def ex11():
    n1 = int(input("digite o primeiro numero (inteiro):\n"))
    n2 = int(input("digite o segundo numero (inteiro):\n"))
    n3 = float(input("digite o terceiro numero (real): \n"))
    print("o produto do dobro do primeiro com metade do segundo: {}".format((n2/2)*n1)) 
    print("a soma do triplo do primeiro com o terceiro: {}".format((n1*3)+n3))
    print("terceiro ao cubo: {}".format(n3**3))

def ex12():
    altura = float(input("digite a altura de uma pessoa:\n"))
    print("o peso ideal desta pessoa é de: {} kilos".format((72.7*altura)-58))

def ex13():
    altura = float(input('digite sua altura :\n'))
    sexo = input('digite seu sexo :\n')
    peso = float(input('digite seu peso :\n'))
    if sexo == 'h':
        peso_ideal = (72.7*altura)-58
        print('peso ideal {}'.format(peso_ideal))
        if peso > peso_ideal:
            print('você está acima do peso')
        elif peso < peso_ideal:
            print('você está abaixo do peso')
        elif peso == peso_ideal:
            print('você está no peso ideal')
    elif sexo == 'm':
        peso_ideal =(62.1*altura)-44.7
        print('peso ideal {}'.format(peso_ideal))
        if peso > peso_ideal:
            print('você está acima do peso')
        elif peso < peso_ideal:
            print('você está abaixo do peso')
        elif peso == peso_ideal:
            print('você está no peso ideal')           

  
def ex14():
    peso = float(input("digite o peso de peixes pescados: \n"))
    peso_maximo = 50
    multa = 4
    excesso = (peso - peso_maximo) * multa
    if peso > peso_maximo:
        print("valor da multa é de: {} reais".format(excesso))
    else:
        print("nao precisa pagar multa.\n")

def ex15():
    salario_hora = float(input("digite o salario que ganha por hora:\n"))
    horas_trabalhadas = int(input("digite o numero de horas trabalhadas no mes:\n"))
    total_salario = salario_hora * horas_trabalhadas
def ex15():
    salario_hora = float(input("digite quanto vc ganha por hora:"))
    horas_trabalho = int(input("digite as horas trabalhadas por mes:"))
    
    salario_bruto = salario_hora * horas_trabalho 
    imposto_renda = salario_bruto * 0.11
    inss = salario_bruto * 0.08    
    sindicato = salario_bruto * 0.05
    descontos = imposto_renda + inss + sindicato
    salario_liquido = salario_bruto - descontos
    
    print("o salario bruto é: {}\n".format(salario_bruto))
    print("o total de desconto de imposto de renda é: {}\n".format(imposto_renda))
    print("o total de desconto de inss é:{}\n".format(inss))
    print("o total de desconto de sindicato é:{}\n".format(sindicato))
    print("o salario liquido é:{}\n".format(salario_liquido))


    
    
    
