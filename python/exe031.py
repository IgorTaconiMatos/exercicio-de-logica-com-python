num = int(input("Digite um número para saber sua tabuada: "))

# repetir 10 vezes
for mult in range(1, 11):
    # escrever o input do usuáro, a variavel multiplicação e multiplicar as duas anteriores
    print(f"{num} x {mult:2} = {num * mult:2}")
