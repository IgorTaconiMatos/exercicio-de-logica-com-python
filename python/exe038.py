id_total = id_M = quant_F = 0
velho_M = ""

# repetir 4 vezes
for loop in range(1, 5):
    print(f"\nVamos analisar as informações da {loop} pessoa")
    # armazenar informações
    nome = str(input("Nome: ")).strip().capitalize()
    idade = int(input("Idade: "))
    sexo = str(input("Digite M para masculino e F para feminino: ")).strip().upper()
    # armazenar a soma das idade do grupo
    id_total += idade

    # verifocar erro
    if sexo != "M" and sexo != "F":
        print("INFORMAÇÃO INVÁLIDA")
    # armazenar a idade e o nome do homem mais velho
    elif sexo == "M" and idade > id_M:
        id_M = idade
        nome_M = nome
    # armazenar a mulher com menoa de 20 anos
    elif sexo == "F" and idade < 20:
        quant_F += 1

# calcular a media da idade do grupo.
media = id_total / 4

print(
    f"""A média das idades do grupo acima é de {media:.1f}.
O homem mais velho é o {nome_M} com {id_M}.
Tem {quant_F} mulheres que são menores de 20 anos."""
)
