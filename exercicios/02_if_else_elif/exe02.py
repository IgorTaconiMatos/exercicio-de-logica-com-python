"""
Faça um Programa que leia três números inteiros e mostre o maior deles.
"""

primeiro = int(input("Primeiro numero: "))
segundo = int(input("Segundo numero : "))
terceiro = int(input("Terceiro numero: "))
maior = primeiro

if segundo > maior:
    maior = segundo
if terceiro > maior:
    maior = terceiro

print(f"Maior: {maior}")
