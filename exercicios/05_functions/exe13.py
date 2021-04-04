"""
Faça um algoritmo que receba dois números e descubra seu MMC.
"""


def mmc(a, b):
    mmc = int(a * b / mdc(a, b))
    return mmc


def mdc(a, b):
    while True:
        resto = a % b
        a = b
        b = resto
        if resto == 0:
            break
    return a


num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
mmc = mmc(num1, num2)
print(f"O MMC de {num1} e {num2} é {mmc}")
