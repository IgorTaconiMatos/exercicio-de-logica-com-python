"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

a = float(input("Primeiro segmento: "))
b = float(input("Segunduo segmento: "))
c = float(input("Terceiro segmento: "))

# formula do para verificar se pode ser formado um triângulo
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print("Pode ser um triângulo")
else:
    print("Não é um triângulo")
