"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

geral = []
aluno = []
notas = []
soma_notas = média = 0

while True:
    # adicionar nome
    aluno.append(str(input("Nome: ")).strip().capitalize())
    # adicionar notas
    notas.append(int(input("Nota 1: ")))
    notas.append(int(input("Nota 2: ")))
    # calcular média
    for nota in notas:
        soma_notas += nota
    média = soma_notas / 2
    # adicionar notas e média a lista "aluno"
    aluno.append(notas[:])
    aluno.append(média)
    # adicionar aluno a outra lista
    geral.append(aluno[:])
    # limpar lista "aluno" e "notas"
    notas.clear()
    aluno.clear()

    while True:
        # parar ou continuar
        para = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        # verificar opção inválida
        if para in "SN":
            break
    # parar o loop se
    if para in "N":
        break

print(">" * 35)
print(f'{"N°":^2} {"NOME":^7} {"MÉDIA":^15}')
print("-" * 30)
# mostrar imformações formatadas
for pos, bloco in enumerate(geral):
    print(f"{pos:^2} {bloco[0]:^7} {bloco[2]:^15}")
print("-" * 30)

while True:
    # visualizar as notas de um aluno específico
    notas_ind = int(input("Mostra notas de qual aluno? (999 para interromper) "))
    # interromper o laço
    if notas_ind == 999:
        break
    # verificar opção inválida
    elif notas_ind > len(geral) - 1 or notas_ind < 0:
        print("Informação inválida.")
    # mostra as notas do aluno
    else:
        print("-" * 30)
        print(f"Notas de {geral[notas_ind][0]} são {geral[notas_ind][1]}")
        print("-" * 30)
