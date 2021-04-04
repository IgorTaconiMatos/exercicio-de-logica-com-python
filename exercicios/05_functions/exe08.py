"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""


def cont_escada(n):
    numeros = list()
    for cont in range(1, n + 1):
        numeros.append(cont)
        print(*numeros)


cont_escada(10)
