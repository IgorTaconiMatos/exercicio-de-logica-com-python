"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""


def escada(n):
    for degral in range(1, n + 1):
        for cada in range(0, degral):
            print(f"{degral:2}", end=" ")
        print("")


escada(10)
