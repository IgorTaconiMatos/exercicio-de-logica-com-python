"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""

num = cont = soma = 0

#loop com condição
while n < 999:
	#armazenar informação
	num = int(input('Digite um núnero [999 para parar] : '))
	#contar quantas número foram pedidos
	cont += 1
	#somar os números
	soma += n
#mostrar os resultados com uma pequena gambiarra, pois não vale usar o break ainda
print(f'Foram {cont - 1} números digitados e a soma desses valores é igual a {soma - 999}')
