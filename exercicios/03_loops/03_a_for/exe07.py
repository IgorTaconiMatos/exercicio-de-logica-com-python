"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

# pedir número
num = int(input("Digite um valor: "))
cont = 0

for verifica in range(1, num + 1):
    # verificar se o número é divisível por "verifica"
    if not num % verifica:
        # contar quantas vezes foi divisível
        cont += 1
        # mostrar valor que é divisível
        print(verifica, end=" ")

# se contador for igual a 2, é primo
if cont == 2:
    sera = "ele É"
# se não, não é primo
else:
    sera = "NÃO é"

# mostrar resultado
print(f"\nO número {num} é divisivel pelos número acima, portanto, {sera} primo")
