"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""

cont = soma = maior = 0
para = ''

#loop condicional
while 'N' not in para:
	#armazenar informação
	num = int(input('Digite um número: '))
	#registra quantos números foram digitados para tirar a média depois
	cont += 1
	#somar os números
	soma += num
	#verificar o maior número
	menor = num
	if num >= maior:
		maior = num
	#verificar o menor número
	elif num <= menor or num <= maior:
		menor = num

	#loop condicional
	while 'N' or 'S' not in para:
		#parar ou continuar
		para = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

#calcular média
média = soma / cont
#mostra informações
print(f'Você digitou {cont} números e a média foi {média}.')
print(f'O maior valor foi {maior} e o menor valor foi {menor}')
