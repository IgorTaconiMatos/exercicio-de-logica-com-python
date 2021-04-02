"""
Faça o usuário informar um  pedir um número(N). O programa deve escrever os números de 1 até N. Se o número é divisível por 3, no lugar do número escreva Fizz. Se o número é divisível por 5, no lugar do número escreva Buzz. Se o número é divisível por 3 e 5, no lugar do número escreva FizzBuzz
"""

def fizzbuzz(n):
	for num in range(1, n + 1):
		if not num % 15:
			print('fizzbuzz')
		elif not num % 3:
			print('fizz')
		elif not num % 5:
			print('buzz')
		else:
			print(num)


valor = int(input('Informe o fim da contagem: '))
fizzbuzz(valor)
