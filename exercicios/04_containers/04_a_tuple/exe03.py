"""
Crie um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:
a)Quantas vezes apareceu o 9.
b)Em que posição foi digitado o primeiro valor 3.
c)Quais foram os números pares.
"""

# criar um input dos valores dentro da tupla
num = (
    int(input("Digite um valor: ")),
    int(input("Digite mais um valor: ")),
    int(input("Digite outro valor: ")),
    int(input("Digite um último valor: ")),
)

# contar quantas vezes o 9 aparece
print("O número 9 apareceu {} vezes".format(num.count(9)))
# se o 3 estiver na lista
if 3 in num:
    # mostrar em qual posição ele foi digitado
    print("O número 3 apareceu na {} posição".format(num.index(3) + 1))
# senão, informe que não tem nenhum 3 na tupla
else:
    print("O número 3 não foi digitado")
print("Apareceram os seguintes números pares: ", end="")
# varrer a tupla
for n in range(0, 4):
    # verificar se é par
    if not num[n] % 2:
        # mostrar os números pares
        print(num[n], end=" ")
