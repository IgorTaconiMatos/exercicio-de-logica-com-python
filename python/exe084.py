# definir função com *args parâmetros
def maior(*args):
    maior = 0
    # veridicar cada parâmetro passado
    for verifica in args:
        # armazenar o maior valor
        if verifica > maior:
            maior = verifica
    # retornar o maior valor
    return maior


print(maior(12, 30, 26, 18, 1, 4, 50, 2))
print(maior(1, 23, 34, 23, 21, 10, 32))
print(maior(244, 23, 8, 3, 23, 123))
print(maior(12, 23, 24, 145, 45))
print(maior(23, 98, 767, 66))
print(maior(12, 34, 45))
print(maior(23, 874))
print(maior(34))
print(maior())
