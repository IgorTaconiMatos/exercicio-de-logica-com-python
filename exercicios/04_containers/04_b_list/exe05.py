"""
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

num = []
impar = []
par = []

while True:
    # adicionar valor
    num.append(int(input("Digite um valor: ")))
    while True:
        # parar ou continuar
        parar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        # verificar opção inválida
        if parar in "SN":
            break
    # parar loop
    if "N" in parar:
        break

# acessar cada valor da lista
for valor in num:
    # verificar se o valor é par
    if not valor % 2:
        # adicionar valor a lista par
        par.append(valor)
    # senão
    else:
        # adicionar valor a lista impar
        impar.append(valor)

print(">" * 40)
# mostrar as listas
print(f"A lista completa é {num}")
print(f"A lista de pares é {par}")
print(f"A lista de ímpates é {impar}")
