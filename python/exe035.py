# armazenar a string, tirar os espaço desnecessários, colocar tudo em minúsculo e remover os espaços.
frase = str(input("Digite a frase: ")).strip().lower().replace(" ", "")
# ira receber a frase ao contrario em branco.
contrario = str("")

# varrer a variável ao contrário.
for varre in frase[::-1]:
    # adicionar o que for varrido para o contador.
    contrario += varre
# verificar se contrario é igual a frase.
if contrario == frase:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
