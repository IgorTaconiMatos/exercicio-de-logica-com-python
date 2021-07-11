# armazenar notas
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))
# calcular a média
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média é {media:.2f}.")
# informar a situação conforme a média
if media >= 7.0:
    print("Você foi APROVADO.")
elif media >= 5.0:
    print("Você está de RECUPERAÇÃO.")
else:
    print("Você foi REPROVADO.")
