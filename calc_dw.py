def soma(*args):
        resultado = 0
    for num in args:
        resultado += num
    return print(f"O resultado da soma dos valores digitado é: {resultado} ")


def sub(*args):


def mult(*args):


def div(*args):


def calc():
    print("Seja bem vindo a calculadora estudantil!")
    print("As operações possiveis são:")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    resp = int(input("Escolha a operação a ser usada (1 a 4): "))
    if resp not in [1, 2, 3, 4]:
        print("Opção não encontrada!")
        resp = int(input("Escolha a operação a ser usada (1 a 4): "))
