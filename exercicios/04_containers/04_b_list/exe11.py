"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""

from random import randint
from time import sleep

numeros = []

print("-" * 30)
print(f'{"JOGA NA MEGA SENA": ^30}')
print("-" * 30)

# quantidade de jogos a serem gerados
jogos = int(input("Quantos jogos você quer que eu sorteie? "))

# gerar jogos pedidos.
for jogo in range(1, jogos + 1):
    # tamanho limite de cada jogo.
    while len(numeros) < 6:
        # gerar um números aleatório.
        num = randint(0, 60)
        # verificar se o números já está na lista.
        if num not in numeros:
            # adicionar o número na lista.
            numeros.append(num)
    # ordenar a lista.
    numeros.sort()
    print(f"Jogo {jogo}: {numeros}")
    sleep(1)

    # limpar a lista
    numeros.clear()

print(f'{" < BOA SORTE! > ":-^30}')
