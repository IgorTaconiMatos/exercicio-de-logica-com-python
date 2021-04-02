"""
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""

pessoa = {}
grupo = []
mulheres = []
cont = soma_idade = 0

while True:
	#armazenar informações pessoais.
	pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
	pessoa['sexo'] = str(input('Sexo [F/M] ')).strip().upper()[0]
	#verificar informação inválida.
	while pessoa['sexo'] not in 'FM':
		print('Informação inválida')
		pessoa['sexo'] = str(input('Sexo [F/M] ')).strip().upper()[0]
	#armazenar as pessoas do sexo F.
	if 'F' in pessoa['sexo']:
		mulheres.append(pessoa['nome'][:])
	pessoa['idade'] = int(input('Idade: '))
	#somar as idades.
	soma_idade += pessoa['idade']
	#adicionar o dicionário a lista.
	grupo.append(pessoa.copy())
	#contar quantas pessoas cadastradas.
	cont += 1
	#parar ou continuar
	para = str(input('Quer continuar? [S/N] ')).strip().upper()
	#verificar informação inválida.
	while para not in 'SN':
		print('Informação inválida')
		para = str(input('Quer continuar? [S/N] ')).strip().upper()
	if 'N' in para:
		break

#mostrar as informação.
print('>' * 35)
print(f'— O grupo tem {cont} pessoas.')
print(f'— A média de idade é {soma_idade / cont} anos')
#se a lista mulheres for maior que 0, mostre os nomes.
if len(mulheres) > 0:
	print(f'— As mulheres cadastradas foram: ', end='')
	for v in mulheres:
		print(v, end= '. ')
else:
	print('— Não foram cadastradas mulheres.', end='')

print('\n— Lista das pessoas que estão acima da média:')
#ler cada dicionário
for dic in grupo:
	#se idade do dicionário for maior que a média.
	if dic['idade'] > soma_idade / cont:
		#mostrar chave e valor de cada lista.
		for k, v in dic.items():
			print(f'{k} = {v};', end=' ')
		print('\n')
print('<<<ENCERRADO>>>')
