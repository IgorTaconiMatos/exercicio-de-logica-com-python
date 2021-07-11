# definir função com parâmetros
def área(largura, comprimento):
    # retornar a multiplicação dos parâmetros
    return largura * comprimento


# armazenar as informações
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))
# chamar a função
area = área(largura, comprimento)

# mostrar informações
print(f"A área de um terreno {largura}x{comprimento} é de {area}m².")
