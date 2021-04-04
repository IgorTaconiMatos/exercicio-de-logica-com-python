"""
Um número é dito perfeito quando ele é igual a soma de seus fatores. Por exemplo, os fatores de 6 são 1, 2 e 3 (ou seja, podemos dividir 6 por 1, por 2 e por 3) e 6=1+2+3, logo 6 é um número perfeito. Escreva uma função que recebe um inteiro e dizer se é perfeito ou não. Em outra função, peça um inteiro n e mostre todos os números perfeitos até n.
"""


def numeroPerfeito(numero):
    soma_fatores = 0
    for fator in range(1, numero):
        if not numero % fator:
            soma_fatores += fator

    if numero == soma_fatores:
        return True
    else:
        return False


def numerosPerfeitos(numero):
    perfeitos = []
    for teste in range(1, numero + 1):
        verifica = numeroPerfeito(teste)
        if verifica:
            perfeitos.append(teste)

    return perfeitos


teste1 = int(input("Informe um número: "))
perfeito = numeroPerfeito(teste1)
print(f"O número {teste1} é", end=" ")
print("perfeito" if teste1 is True else "imperfeito")
print("—" * 40)
teste2 = int(input("Informe um valor para saber todo os números perfeitos até ele: "))
total_perfeitos = numerosPerfeitos(teste2)
print(f"Os números perfeitos no intervalo de 1 a {teste2} são:", end=" ")
print(*total_perfeitos)
