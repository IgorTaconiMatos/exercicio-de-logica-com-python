"""
Faça un algoritmo que calcule a soma dos N primeiros números primos, sendo N definido pelo usuário.
"""


def primo(n):
    if n == 2:
        return True
    elif n <= 1 or not n % 2:
        return False
    else:
        cont = 0
        for num in range(3, n + 1):
            if not n % num:
                cont += 1
        if cont == 1:
            return True


def soma_primos(n):
    soma = 0
    for num in range(2, n + 1):
        ver = primo(num)
        if ver is True:
            soma += num
    return soma


intervalo = int(input("Digite um valor: "))
soma = soma_primos(intervalo)
print(f"A soma dos números primos de 2 até {intervalo} é {soma}")
