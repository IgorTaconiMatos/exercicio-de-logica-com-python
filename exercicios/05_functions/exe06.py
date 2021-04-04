"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint
from time import sleep


# definir função com um parâmetro
def sorteia(lista):
    # criar um loop de 5 iterações
    for sorteio in range(0, 5):
        # adicionar valor sorteado a lista
        lista.append(randint(0, 10))
    # retornar a lista
    return lista


# definir função com um parâmetro
def somaPar(lista):
    soma = 0
    # retornar cada valor da lista em verifica
    for verifica in lista:
        # verificar se o valor é par
        if not verifica % 2:
            # somar os valores pares
            soma += verifica
    # retornar a variável soma
    return soma


números = []

# sortear 5 valores e armazena-los na lista números
sorteados = sorteia(números)
# somar os valores pares da lista números
soma = somaPar(números)

# mostrar os resultados
print("Os números sorteados foram:", end=" ")
for valor in sorteados:
    print(valor, end=" ", flush=True)
    sleep(0.5)
print(f"\nA soma dos números pares é: {soma}")
