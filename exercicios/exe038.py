"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""

#variaveis a serem manipuladas.
maior = 0
menor = 1000

#repetir do 1 ao 5.
for pess in range(1, 6):
	#armazenar o peso da pessoa.
	peso = float(input(f'Peso da {pess} pessoa: (kg) '))
	#verificar se peso é maior que a variá vel maior.
	if peso >= maior:
		maior = peso
	#verificar se peso é menor que a variá vel menor.
	elif peso <= menor:
		menor = peso
		
print(f'O maior peso informado foi {maior} e o menor foi {menor}.')
