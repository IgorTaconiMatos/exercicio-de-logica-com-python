"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

real = float(input('Quantos dinheiro você tem na carteira? R$'))
dolar = real / 5.31

print(f'Com R$ {real:.2f} você pode comprar USD {dolar:.2f}.')
