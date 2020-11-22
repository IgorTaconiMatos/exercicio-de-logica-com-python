"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
"""

#obter preço da comprar
preco = float(input('Preço da compra: R$'))
print('''FORMA DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
#obter forma de pagamento
opcao = int(input('Sua opção é... : '))
print(f'O preço é R${preco:.2f}')

#opção 1
if opcao == 1:
	print(f'Pagando à vista no dinheiro ou no cheque você ganha um desconto de 10% totalizando o preço da compra em R${preco - (preco * 0.1):.2f}.')
#opção 2 
elif opcao == 2:
	print(f'Pagando à vista no cartão você ganha um desconto de 5% totalizando o preço da compra em R${preco - (preco * 0.05):.2f}.')
#opção 3
elif opcao == 3:
	print('Parcelando em 2x no cartão o preço da compra não se altera.')

#opção 4
elif opcao == 4:
	print('''Você pode parcelar em
3x ou 4x com 10% de acréscimo,
5x ou 6x com 15% de acréscimo, 
7x ou 8x com 20% de acréscimo e
9x ou 10x com 25% acréscimo''')
	#obter quantidade de parcelas
	parcelas = int(input('Em quantos vezes deseja parcelar? '))
	#se 3 ou 4 parcelas
	if parcelas == 3 or parcelas == 4:
		#preço por mês com 10% de juros no valor total
		mes = (preco * 0.1 + preco) / parcelas
		print(f'Sua compra será parcelada em {parcelas}x de R${mes:.2f} com JUROS de 10%')
		print(f'Sua compra de R${preco:.2f} vai custar R${mes * parcelas:.2f} no final.')
	#se 5 ou 6 parcelas
	elif parcelas == 5 or parcelas == 6:
		mes = (preco * 0.15 + preco) / parcelas
		print(f'Sua compra será parcelada em {parcelas}x de R${mes:.2f} com JUROS de 15%')
		print(f'Sua compra de R${preco:.2f} vai custar R${mes * parcelas:.2f} no final.')
	elif parcelas == 7 or parcelas == 8:
		mes = (preco * 0.2 + preco) / parcelas
		print(f'Sua compra será parcelada em {parcelas}x de R${mes:.2f} com JUROS de 20%')
		print(f'Sua compra de R${preco:.2f} vai custar R${mes * parcelas:.2f} no final.')
	elif parcelas == 9 or parcelas == 10:
		mes = (preco * 0.25 + preco) / parcelas
		print(f'Sua compra será parcelada em {parcelas}x de R${mes:.2f} com JUROS de 25%')
		print(f'Sua compra de R${preco:.2f} vai custar R${mes * parcelas:.2f} no final.')
	#se mais de 10 parcelas ou menos de 3
	else:
		print('\nINFORMAÇÃO INVÁLIDA')

#se opção de pagamento diferente das opção dadas
else:
	print('\nINFORMAÇÃO INVÁLIDA')
