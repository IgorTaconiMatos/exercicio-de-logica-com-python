"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""

jogador = {}
total_gols = []
soma_gols = 0

#criar chave adicionando valor
jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()
#informar número de partidas
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
#uma iteração para cada partida
for quant in range(0, partidas):
	#informar a quantidade de gols por partida
	gols = int(input(f'Quantos gols na partida {quant}: '))
	#adicionar quantidade de gols na lista
	total_gols.append(gols)
	#somar o total de gols
	soma_gols += gols
#criar chaves adicionando valores
jogador['gols'] = total_gols
jogador['total'] = soma_gols

print('>' * 35)
#mostrar informações formatadas
for k, v in jogador.items():
	print(f'O campo {k} tem o valor {v}')
print('>' * 35)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
#mostrar a quantidade de gols por partida
for v in range(0, len(jogador['gols'])):
	print(f'  =>Na partida {v}, fez {jogador["gols"][v]} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
