soma = cont = 0
# varrer todo os números ímpares até o 500
for num in range(1, 500, 2):
    # verificar se o número é múltiplo de 3
    if not num % 3:
        # ver o total de números que múltiplos de 3
        cont += 1
        # somar os números
        soma += num
print(f"A soma de todos os {cont} números múltiplos de 3 e que são ímpares é {soma}")
