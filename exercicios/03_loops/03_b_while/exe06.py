"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep

# armazenar os valores.
num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
# variáviel do loop
escolha = 0
while escolha != 5:
    # opções e suas ações.
    print(
        """[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa"""
    )
    # armazenar esolha do usuário.
    escolha = int(input("Qual é a sua opção?: "))
    # somar.

    if escolha == 1:
        print(f"A soma de {num1:.1f} + {num2:.1f} é {num1 + num2:.1f}.")
    # multiplicar.
    elif escolha == 2:
        print(f"A multiplicação de {num1:.1f} x {num2:.1f} é {num1 * num2:.1f}.")
    # mostrar o maior número
    elif escolha == 3:
        print(f"O entre {num1} e {num2} o maior é {max(num1, num2)}.")
    # digitar novos valores.
    elif escolha == 4:
        print("Informe os números novamente:")
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
    # verificar erro.
    elif escolha <= 0 or escolha >= 6:
        print("Opção inválida.")
    print("=-" * 6)
    sleep(1)
print("Obrigado por usar nossa calculadora.\nVolte sempre.")
