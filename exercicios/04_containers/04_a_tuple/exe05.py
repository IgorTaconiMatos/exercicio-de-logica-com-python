'''
Crie um programa que tenha uma tuplas única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

#criar tupla com os produtos e os preços
produtos = ('Cueca', 15, 'Bermuda', 20, 'Calça', 50, 'Camisa', 50, 'Camiseta', 50, 'Blusa', 75, 'Tênis', 100, 'Chinelo', 20, 'Boné', 40)

print('-' * 25)
#criar um loop do tamanho da tupla
for unidade in range(0, len(produtos)):
	#se o índice for par será o produto, imprima
	if not unidade % 2:
		print(f'{produtos[unidade]:.<30}R$', end='')
	#senã, o índice é o preço
	else:
		print(f'{produtos[unidade]:>6.2f}')
print('-' * 25)
