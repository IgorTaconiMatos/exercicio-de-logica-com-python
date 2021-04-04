"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

total = mil = 0

print("—" * 18)
print("LOJA SUPER BARATÃO")
print("—" * 18)

while True:
    nome = str(input("Nome do Produto: ")).strip().capitalize()
    preco = float(input("Preço: R$"))

    total += preco
    barato = preco
    ba_nome = nome

    if preco >= 1000:
        mil += 1
    if preco < barato:
        barato = preco
        ba_nome = nome

    para = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while para not in "SN":
        print("Informação inválida")
        para = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if "N" in para:
        break

print("—" * 12, "FIM DO PROGRAMA", "—" * 12)
print(
    f"""O total da compra foi R${total:.2f}.
Temos {mil} produtos custando mais de R$1000.00.
O produto mais barato foi {ba_nome} que custa R${barato:.2f}"""
)
