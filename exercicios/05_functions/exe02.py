"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
"""


# definir função com parâmetros
def escreva(texto):
    # colocar uma linha em cima do texto do tamanho do mesmo
    print("-" * len(texto))
    # escrever texto
    print(texto)
    # colocar um linha embaixo do texto do tamanho do mesmo
    print("-" * len(texto))


# armazenar informação
título = input("Escreva o título: ")
# chamat função
escreva(título)
