"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salário = float(input('Qual é o salário do funcionário? R$'))
ajuste = salário + salário * 0.15

print(f'Um funcionário que ganhava R${salário:.2f}, com 15% de aumento, passa a receber R${ajuste:.2f}.')
