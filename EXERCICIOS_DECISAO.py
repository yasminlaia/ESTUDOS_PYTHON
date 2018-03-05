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

