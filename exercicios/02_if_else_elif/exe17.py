"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint

# armazenar o número do computador
comp = randint(1, 3)
# armazenar escolha do usuário
print(
    """Suas opções:
[1] Pedra
[2] Papel
[3] Tesoura"""
)
voce = int(input("Qual é a sua jogada? "))

# verificar informações e apresentar o resultado
if comp == voce:
    print(f"EMPATE. Os dois escolheram {voce}.")
elif comp == 1 and voce == 2:
    print("Você GANHOU! O computador escolheu Pedra")
elif comp == 1 and voce == 3:
    print("Você PERDEU! O computador escolheu Pedra")
elif comp == 2 and voce == 1:
    print("Você PERDEU! O computador escolheu Papel")
elif comp == 2 and voce == 3:
    print("Você Ganhou! O computador escolheu Papel")
elif comp == 3 and voce == 1:
    print("Você Ganhou! O computador escolheu Tesoura")
elif comp == 3 and voce == 2:
    print("Você PERDEU! O computador escolheu Tesoura")
