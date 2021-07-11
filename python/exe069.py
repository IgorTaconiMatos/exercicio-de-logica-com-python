grupo = []
dados = []
pessoas = maior = menor = 0
maior_pessoas = []
menor_pessoas = []

while True:
    # coleta de dados.
    dados.append(str(input("Nome: ")).strip().capitalize())
    dados.append(float(input("Peso: ")))
    grupo.append(dados[:])
    dados.clear()
    pessoas += 1

    # para ou continue a coleta.
    escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while escolha not in "SN":
        print("Informação inválida")
        escolha = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if "N" in escolha:
        break

print(f"Ao todo, você cadastrou {pessoas} pessoas.")

# armazenar o maior valor.
for bloco in grupo:
    if bloco[1] >= maior:
        maior = bloco[1]
        menor = maior
# armazenar os nomes que tem o maior valor.
for bloco in grupo:
    if maior in bloco:
        maior_pessoas.append(bloco[0])
print(f"O maior peso foi {maior}kg. Peso de {maior_pessoas}.")

# armazenar o menor valor.
for bloco in grupo:
    if bloco[1] <= menor:
        menor = bloco[1]
# armazenar os nomes que tem o menor valor.
for bloco in grupo:
    if menor in bloco:
        menor_pessoas.append(bloco[0])
print(f"O maior peso foi {menor}kg. Peso de {menor_pessoas}.")
