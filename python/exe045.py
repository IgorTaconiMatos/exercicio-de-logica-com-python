num = int(input("Digite um número para calcular o seu fatorial: "))
# copiar o número
cont = num
fatorial = num

# enquanto contador for maior que 1
while cont != 1:
    # calcular fatorial subtraindo o número e multiplicando em seguida
    cont -= 1
    fatorial = fatorial * cont
print(f"Calculando {num}! =", end=" ")

# mostrar números que foram multiplicados e o resultado
for cont in range(num, 0, -1):
    print(f"{cont} x", end=" ")
print(f"= {fatorial}.")
