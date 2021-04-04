"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

print("-=" * 12)
print("Vamos jogar par ou ímpar")
print("-=" * 12)
cont = 0

while True:
    voce = int(input("Digite um valor: "))
    comput = randint(0, 10)
    total = comput + voce

    escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    while escolha not in "PpIi":
        print("Informação inválida. Tente novamente.")
        escolha = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]

    if total % 2 == 0:
        result = "DEU PAR"
    else:
        result = "DEU ÍMPAR"
    if escolha == "P" and "PAR" in result.split():
        resp = "VENCEU"
        cont += 1
    elif escolha == "I" and "ÍMPAR" in result.split():
        resp = "VENCEU"
        cont += 1
    else:
        resp = "PERDEU"

    print(
        f"Você jogou {voce} e o computador jogou {comput}. Total de {total} de {result}."
    )
    print(f"Você {resp}.")

    if "PERDEU" in resp:
        print("-=" * 12)
        print(f"GAME OVER! Você venceu {cont} vezes.")
        break

    print("Vamos jogar novamente...")
