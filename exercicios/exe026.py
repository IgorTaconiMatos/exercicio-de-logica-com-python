"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

#armazenar informações
massa = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = massa / (altura * altura)

print(f'''O seu peso é {massa}kg e sua altura é {altura}m.
O seu IMC é {imc:.2f}.''')
#informar a situação do IMC conforme o seu valor
if imc > 40:
	print(f'IMC acima de 40 é considerado OBESIDADE MÓRBIDA')
elif imc > 30:
	print('IMC entre 30 e 40 é considerado OBESIDADE')
elif imc > 25:
	print('IMC entre 25 e 30 é considerado SOBREPESO')
elif imc > 18.5:
	print('IMC entre 18.5 e 25 é considerado PESO IDEAL')
else:
	print('IMC abaixo de 18.5 é considerado ABAIXO DO PESO')
