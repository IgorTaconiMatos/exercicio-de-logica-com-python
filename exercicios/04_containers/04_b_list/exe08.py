"""
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
"""

numeros = [[], []]

# armazenar valores
for valor in range(1, 8):
    num = int(input(f"Digiete o {valor}° valor: "))
    # verificar se é par e adicionar no índice 0
    if not num % 2:
        numeros[0].append(num)
    # se não for par, adicione no índice 1
    else:
        numeros[1].append(num)

# ordenar as listas
numeros[0].sort()
numeros[1].sort()
# mostrar os resultados
print(f"Os valores pares digitados foram: {numeros[0]}")
print(f"Os valores ímpares digitados foram {numeros[1]}")
