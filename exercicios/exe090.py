"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""

def valor_pagamento(valor, dias):
	if dias == 0:
		return valor
	else:
		juros_dia = dias * 0.001
		multa = valor * 0.03
		valor += multa + juros_dia
		return valor


quant = total = 0

while True:
	valor_prestacao = float(input('Valor da prestação. (0 para encerrar) R$'))
	if valor_prestacao == 0:
		break
	dias_atraso = int(input('Dias de atraso. '))
	
	novo_valor = valor_pagamento(valor_prestacao, dias_atraso)
	print(f'Você tem que pagar R${novo_valor:.2f}')
	total += novo_valor
	quant += 1

print('—'*40)
print(f'Foram realizados {quant} pagamentos no valor total de R${total:.2f}.')
