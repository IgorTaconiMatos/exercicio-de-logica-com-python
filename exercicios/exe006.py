"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
preço = float(input('Qual o preço do produto? R$'))
ajuste = preço - preço * 0.05

print(f'O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar R${ajuste:.2f}')
