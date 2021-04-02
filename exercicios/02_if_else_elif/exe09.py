"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

casa = float(input('Valor da casa: R$'))
salario = float(input('Seu salário: R$'))
anos = int(input('Quantos anos de financiamento? '))
#valor das parcelas por mês.
mes = casa / (anos * 12)

#se as parcelas forem menores que 30% do salário.
if mes <= salario * 0.3:
	print(f'O preço da casa é R${casa:.2f}.\nPagando em {anos} anos seram {anos * 12} meses.\nCada parcela mensalmente será no valor de R${mes:.2f}.')
	print('Empréstimo APROVADO.')
#se as parcelas forem maiores que 30% do salário.
else:
	print(f'O preço da casa é R${casa:.2f}.\nPagando em {anos} anos seram {anos * 12} meses.\nCada parcela mensalmente será no valor de R${mes:.2f}.')
	print('Empréstimo REPROVADO.')
