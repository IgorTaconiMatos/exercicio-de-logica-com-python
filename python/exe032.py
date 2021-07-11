soma_par = 0

# repete 6 vezes.
for leia in range(0, 6):
    número = int(input("Digite um número inteiro: "))
    # verificando se é par.
    if número % 2 == 0:
        # somar os números pares e guarda-los.
        soma_par += número
print(f"A soma de todos os números pares é {soma_par}")
