cont = 0

# armazenar a variável N termos
n = int(input("Quantos termos? "))
f1 = 1
f2 = 0
f3 = f1 + f2

# loop com condição
while cont < n:
    # mostra o número de Fibonacci
    print(f3, end=" ")
    # modificar condição
    cont += 1
    # realição a soma para saber o próximo número
    f1 = f2
    f2 = f3
    f3 = f1 + f2
