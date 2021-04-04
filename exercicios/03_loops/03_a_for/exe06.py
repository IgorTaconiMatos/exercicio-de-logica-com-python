"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

# pedir o primeiro termo e a razão da PA
primeiro = int(input("Primeiro termo da PA: "))
razão = int(input("Razão da PA: "))
# calculo para mostrar dez termos
decimo = primeiro + (10 - 1) * razão

# mostrar os termos
for termo in range(primeiro, decimo + razão, razão):
    print(termo, end=" => ")
print("Fim!")
