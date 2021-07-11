# inicair loop
sexo = ""
while sexo != "M" and sexo != "F":
    # armazenar informação
    sexo = str(input("Informe seu sexo: [M/F]")).strip().upper()
    # verificar erro
    if sexo != "M" and sexo != "F":
        print("Informação inválida. Tente novamente")
print("Informação armazenada")
