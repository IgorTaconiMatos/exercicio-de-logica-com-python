matriz = [[[], [], []], [[], [], []], [[], [], []]]

# loop para cada linha
for linha in range(0, 3):
    # em cada coluna
    for coluna in range(0, 3):
        # pedir um valor
        número = int(input(f"Digite um valor para [{linha}, {coluna}]: "))
        # inserir o número
        matriz[linha][coluna].insert(coluna, número)

print("-=" * 20)
# loop para cada linha
for linha in matriz:
    print("\n")
    # loop para cada coluna
    for coluna in linha:
        # mostrar valor
        print(coluna, end=" ")
