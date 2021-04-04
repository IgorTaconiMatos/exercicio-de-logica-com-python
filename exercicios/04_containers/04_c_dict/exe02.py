"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""

from operator import itemgetter
from random import randint
from time import sleep

jogos = {}
ranking = {}

print("VALORES SORTEADOS")
# repetir os comandos identados 4 vezes
for número in range(1, 5):
    # criar chave "jogador"(alterando o final do nome a cad loop) e adicionar um valor aleatório
    jogos[f"jogador{número}"] = randint(1, 6)

# mostrar os resultados
for chave, valor in jogos.items():
    print(f"  O {chave} tirou {valor}")
    sleep(1)

# ordenar os jogos pelos valores em ordem decrescente
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print("RANKING DOS JOGADORES")
# mostrar os valores formatados
for chave, valor in enumerate(ranking):
    print(f"  {chave + 1}° lugar: {valor[0]} com {valor[1]}")
    sleep(1)
