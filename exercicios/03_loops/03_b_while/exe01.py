"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

#inicair loop
sexo = ''
while sexo != 'M' and sexo != 'F':
	#armazenar informação
	sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()
	#verificar erro
	if sexo != 'M' and sexo != 'F':
		print('Informação inválida. Tente novamente')
print('Informação armazenada')
