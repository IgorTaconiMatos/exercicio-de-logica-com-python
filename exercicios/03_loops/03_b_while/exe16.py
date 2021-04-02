"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 
"""

cont = maior = quant_M = menor_F = 0

while True:
	idade = int(input('Qual a sua idade? '))
	sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
	while sexo not in 'MF':
		print('Informação inválida. Digite novamente.')
		sexo = str(input('Qual o seu sexo? [M/F')).strip().upper()[0]
	cont += 1
	if idade >= 18:
		maior += 1
	if sexo == 'M':
		quant_M += 1
	if sexo == 'F' and idade < 20:
		menor_F += 1

	para = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	while para not in 'SN':
		print('Informação inválida. Digite novamente.')
		para = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if 'N' in para:
		break

print('-=' * 14)
print(f'''Foram registradas {cont} pessoas,
{maior} são maiores de 18 anos,
{quant_M} são homens e 
{menor_F} são mulheres menores de 20 anos''')
