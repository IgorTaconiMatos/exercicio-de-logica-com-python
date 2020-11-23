"""
Faça um programa que leia e valide as seguintes informações:
A) Nome: maior que 3 caracteres;
B) Idade: entre 0 e 150;
C) Salário: maior que zero;
D) Sexo: 'f' ou 'm';
E) Estado Civil: 's', 'c', 'v', 'd';
"""

#armazenar nome
nome = str(input('Nome: ')).strip().capitalize()
#enquanto o tamanho do nome for menor que 3
while len(nome) <= 3:
	nome = str(input('Informação inválida.\nO nome precisa ter mais que 3 caracteres.\nNome: ')).strip().capitalize()

#armazenar nome
idade = int(input('Idade: '))
#verificar erro
while idade < 0 or idade > 150:
	print('Informação inválida.')
	idade = int(input('Idade: '))

#armazenar salário
salario = float(input('Salário: R$'))
#verificar erro
while salario <= 0:
	print('Informação inválida.')
	salario = float(input('Salário: R$'))

#armazenar sexo
sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
#verificar erro
while sexo not in 'MF':
	print('Informação inválida.')
	sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

#armazenar estado civíl
print('''Estado Civil: 
  [C] Casado(a)
  [S] Solteiro(a)
  [V] Viúvo(a)
  [D] Diforciado(a)''')
estado_civil = str(input('Informe: ')) .strip().upper()[0]
#verificar erro
while estado_civil not in 'CSVD':
	print('Informação inválida.')
	print('''Estado Civil: 
  [C] Casado(a)
  [S] Solteiro(a)
  [V] Viúvo(a)
  [D] Diforciado(a)''')
	estado_civil = str(input('Informe: ')) .strip().upper()[0]

print('Informações registradas.')
