"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

# pedir número
num = int(input("Digite um valor em 0 e 10: "))
# enquanto o número for diferente do pedido
while num < 0 or num > 10:
    print("Informação inválida.")
    # pedir número
    num = int(input("Digite um valor em 0 e 10: "))
print(f"Você digitou o valor {num}")
