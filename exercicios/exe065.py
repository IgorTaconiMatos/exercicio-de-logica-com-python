"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""

numeros = []

while True:
	#armazenar número
	num = int(input('Digite um valor: '))
	#se a lista estiver vazia ou o número não estiver na lista
	if len(numeros) == 0 or num not in numeros:
		#adicionar número a lista
		numeros.append(num)
		print('Valor adicionado com sucesso...')
	#senão, escreva que num já existe na lista
	else:
		print('Valor duplicado! Não vou adicionar...')

	#parar ou continiuar
	escolha = str(input('Que continuar? [S/N] ')).strip().upper()[0]
	#loop condicional para verificar erro
	while escolha not in 'SN':
		print('Informação inválida')
		#pedir novamente para parar ou continuar
		escolha = str(input('Que continuar? [S/N] ')).strip().upper()[0]
	#se escolha for "N", pare o loop
	if 'N' in escolha:
			break

print('=' * 40)
print('Você digitou os valores', end=' ')
#colocar os valores da lista em ordem crescente
numeros.sort()
#mostrar os valores
for valor in numeros:
	print(valor, end=' ')
