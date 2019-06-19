def soma(numero1, numero2):
    return numero1 + numero2


def subtracao(numero1, numero2):
    return numero1 + numero2


def multiplicacao(numero1, numero2):
    return numero1 + numero2


def divisao(numero1, numero2):
    return numero1 + numero2


print("Selecione o número da operação que desejar")
print(" 1 - Soma")
print(" 2 - Subtração")
print(" 3 - Multiplicação")
print(" 4 - Divisão")
option = int(input("Digite uma opção (1/2/3/4) para dar continuidade"))
#option = 1
numeroUm = int(input('Digite o primeiro numero'))
numeroDois = int(input('Digite o segundo numero'))
if 1 == option:
    print(numeroUm, "+", numeroDois, "=", soma(numeroUm, numeroDois))

elif 2 == option:
    print(numeroUm, "-", numeroDois, "=", subtracao(numeroUm, numeroDois))

elif 3 == option:
    print(numeroUm, "*", numeroDois, "=", multiplicacao(numeroUm, numeroDois))

elif 4 == option:
    print(numeroUm, "/", numeroDois, "=", divisao(numeroUm, numeroDois))

else:
    print('Opção não valida')
