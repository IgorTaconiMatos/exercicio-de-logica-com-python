"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""

numeros = []

while True:
	#armazenar valor
	numeros.append(int(input('Digite um valor: ')))
	while True:
	#parar ou continuar
		escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
		#verificar opção inválida
		if escolha in 'SN':
			break
	#parar de coletar informações
	if escolha == 'N':
		break

#mostrar quantos item tem na lista
print(f'Você digitou {len(numeros)} elementos.')
#ordenar a lista e inverter a ordem
numeros.sort(reverse = True)
print(f'Os valores em ordem decrescente são {numeros}')
#se 5 estiver na lista
if 5 in numeros:
	print('O valor 5 faz parte da lista.')
#senão estiver
else:
	print('O valor 5 não foi encontrado na lista.')
