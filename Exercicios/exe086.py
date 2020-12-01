"""
Crie uma função para calcular o fatorial de um número. Depois crie uma função para calcular o coeficiênte binomial:
z = n! / k! * (n - k)!
"""

#definir função com parâmetro
def fatorial(num):
	#copiar o número
	fat = 1
	#enquanto contador for maior que 1
	while num > 1:
		#calcular fatorial subtraindo o número e multiplicando em seguida
		fat *= num
		num -= 1
	#retornar valor
	return fat
	
#definir função com parâmetro
def coeficienteBinomial(n, d):
	#verificar erro
	if n < d:
		númeroBinomial = '\n=>ERRO, o N não pode ser menor que P'
	else:
		#calcular coeficiente binomial
		númeroBinomial = fatorial(n) / (fatorial(d) * fatorial(n - d))
	#retornar valor
	return númeroBinomial


print('COEFICIENTE BINOMIAL')
#armazenar informações
primeiro = float(input('Informe o N: '))
segundo = float(input('Informe o P: '))
#calcular número binomial
numBinomial = coeficienteBinomial(primeiro, segundo)
#mostrar informações
print(f'O número binomial de {primeiro} e {segundo} é {numBinomial}.')
