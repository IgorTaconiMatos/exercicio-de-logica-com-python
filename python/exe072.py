matriz = [[[], [], []], [[], [], []], [[], [], []]]
par = soma = maior = 0

# loop para cada linha
for linha in range(0, 3):
    # loop para cada coluna
    for coluna in range(0, 3):
        # pedir um valor
        número = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        # inserir o número
        matriz[linha][coluna].insert(coluna, número)

print("-=" * 20)
# varrer a matriz.
for linha in range(0, len(matriz)):
    print("\n")
    # varrer as listaa da matriz.
    for coluna in range(0, len(matriz)):
        # varrer os valores dentro de cada lista.
        for valor in range(0, 1):
            print(f"[ {matriz[linha][coluna][valor]} ]", end=" ")

        # verificar se é par e somar.
        if not matriz[linha][coluna][valor] % 2:
            par += matriz[linha][coluna][valor]
        # verficar o posição e somar.
        if coluna == 2:
            soma += matriz[linha][coluna][valor]
        # pegar o maior do indíce 1.
        if linha == 1 and max(matriz[1][coluna]) >= maior:
            maior = matriz[linha][coluna][valor]

print("\n")
print("-=" * 20)
# mostrar valores
print(f"A soma dos valores pares é {par}")
print(f"A soma dos valores da terceira coluna é {soma}")
print(f"O maior valor da segunda linha é {maior}")
