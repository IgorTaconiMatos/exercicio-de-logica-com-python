"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Qual o salário do seu funcionário: R$'))

if salario <= 1250:
	#calcular a porcentagem de 15%
	print(f'Quem ganhava R${salario} passa a ganhar R${salario + salario * 0.15:.2f} agora.')
else:
	#calcular a porcentagem de 10%
	print(f'Quem ganhava R${salario} passa a ganhar R${salario + salario * 0.1:.2f} agora.')
