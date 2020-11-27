"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

#tupla com os númeoros escritos
tupla_num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco','seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseseis', 'dezessesete', 'dezoito', 'dezenove', 'vinte')

while True:
	#inicio do loop
	while True:
		#receber número
		num = int(input('Digite um número entre 0 e 20: '))
		#parar loop se condição for atendida
		if 0 <= num <= 20:
			break
		#senão, escreva tente novamente e reinicie o loop
		print('Tente novamente.')
	#informar número digitado
	print(f'Você digitou o número {tupla_num[num]}')

	#parar ou continuar
	para = str(input('Quer tentar novamente [S/N] ')).strip().upper()[0]
	#enquanto a "para" for diferente de "S" ou "N"
	while 'N' != para != 'S':
		#parar ou continuar
		para = str(input('Quer tentar novamente [S/N] ')).strip().upper()[0]
	#para o programa
	if para == 'N':
		break
print('Volte sempre')
	