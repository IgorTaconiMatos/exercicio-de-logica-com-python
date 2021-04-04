"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date

# contadores com 0
maior = 0
menor = 0

# repetir de 1 ao 7
for varre in range(1, 8):
    # armazenar ano de nascimento.
    idade = date.today().year - int(input(f"Ano de nascimeto da {varre} pessoa: "))
    # verificar se é maior de 18 anos.
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f"{maior} pessoas são maiores de idade e {menor} pessoas são menores de idade.")
