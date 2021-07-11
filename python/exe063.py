lista = []

# armazenar diversos valores em uma lista.
for pos in range(1, 6):
    num = [int(input(f"Digite um valor para a posição {pos}: "))]
    lista += num

# escrever os valores.
print("Os números foram: ", end="")
for valor in lista:
    print(valor, end=" ")

# armazenar o maior e o menor valor.
max = max(lista)
min = min(lista)

# informar o maior valor e as posições.
print(f"\nO maior valor digitado é {max} nas posições", end=" ")
for pos, val in enumerate(lista):
    if max == val:
        print(f"{pos + 1}", end="...")
# informar o menor valor e as posições.
print(f"\nO menor valor digitado é {min} nas posições", end=" ")
for po, va in enumerate(lista):
    if min == va:
        print(f"{po + 1}", end="...")
