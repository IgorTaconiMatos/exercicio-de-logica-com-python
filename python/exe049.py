num = cont = soma = 0

# loop com condição
while num < 999:
    # armazenar informação
    num = int(input("Digite um núnero [999 para parar] : "))
    # contar quantas número foram pedidos
    cont += 1
    # somar os números
    soma += num
# mostrar os resultados com uma pequena gambiarra, pois não vale usar o break ainda
print(
    f"Foram {cont - 1} números digitados e a soma desses valores é igual a {soma - 999}"
)
