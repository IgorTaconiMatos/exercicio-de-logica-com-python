"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

print("Digite 3 números que vou lhe mostrar qual é o maior e qual é o menor.")

# guardar os números
num1 = float(input("1° número: "))
num2 = float(input("2° número: "))
num3 = float(input("3° número: "))

# verificar se o 1° é menor que o 2°, e se 2° é menor que o 3°
if num1 <= num2 <= num3:
    print(f"O maior número é {num3} e o menor número é {num1}")
# verificar se o 2° é menor que o 1°, e se 1° é menor que o 3°
if num2 <= num1 <= num3:
    print(f"O maior número é {num3} e o menor número é {num2}")
# verificar se o 3° é menor que o 1°, e se 1° é menor que o 2°
if num3 <= num1 <= num2:
    print(f"O maior número é {num2} e o menor número é {num3}")
# verificar se o 1° é menor que o 3°, e se 3° é menor que o 2°
if num1 <= num3 <= num2:
    print(f"O maior número é {num2} e o menor número é {num1}")
# verificar se o 2° é menor que o 3°, e se 3° é menor que o 1°
if num2 <= num3 <= num1:
    print(f"O maior número é {num1} e o menor número é {num2}")
# verificar se o 3° é menor que o 2°, e se 2° é menor que o 1°
if num3 <= num2 <= num1:
    print(f"O maior número é {num1} e o menor número é {num3}")
