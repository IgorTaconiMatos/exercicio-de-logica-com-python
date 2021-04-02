"""
Crie um programa que gerencie o aproveitamento de varios jogadores de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. Tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
No final, inclua um sistema de visualização de detalhes do aproveitamento de cada jogador.
"""

jogadores = []

while True:
	jogador = {}
	total_gols = []
	soma_gols = 0
	
	#armazenar as informações.
	jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
	partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
	#armazenar quantidade de gols e o total
	for quant in range(0, partidas):
		gols = int(input(f'Quantos gols na partida {quant + 1}: '))
		total_gols.append(gols)
		soma_gols += gols
	jogador['gols'] = total_gols
	jogador['total'] = soma_gols
	#armazenar jogador.
	jogadores.append(jogador.copy())
	while True:
		#parar ou continuar
		para = str(input('Quer continuar? [S/N] ')).strip().upper()
		#verificar opção
		if para in 'SN':
			break
		#se opção inválida
		print('Informação inválida. Digite apenas S ou N')
	#interromper o loop
	if 'N' in para:
		break

print('>' * 40)
print('—' * 40)
print(f'{"cod":>3} {"nome":<15} {"gols":<15} {"total":<15}')
for pos, val in enumerate(jogadores):
	print(f'{pos:>3} {val["nome"]:<15} {str(val["gols"]):<15} {val["total"]:<15}')
print('—' * 40)

while True:
	#definir jogador a ser mostrado os gols
	dados = int(input('Informe o código do jogador para visualizar aproveitamento. (999 para encerrar): '))
	#parar programa
	if dados == 999:
		break
	#verificar erro
	elif dados < 0 or dados > len(jogadores) - 1:
		print('  Código inválido. Tente novamente.')
	#mostrar informações
	else:
		#definir quantidades de partidas
		quant_partidas = len(jogadores[dados]['gols'])
		print(f'O jogador {jogadores[dados]["nome"]} jogou {quant_partidas} partidas.')
		#mostrar a quantidade de gols por partida
		for valor in range(0, len(jogadores[dados]['gols'])):
			print(f'  =>Na partida {valor + 1}, fez {jogadores[dados]["gols"][valor]} gols.')
		print(f'Foi um total de {jogadores[dados]["total"]} gols.\n')
print('')
