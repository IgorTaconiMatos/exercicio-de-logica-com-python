from datetime import date

# calcular a idade
idade = date.today().year - int(input("Ano de nascimento: "))
print(f"O atleta tem {idade} anos.")
# informa a categoria conforme a idade
if idade > 25:
    categ = "Master"
elif idade > 19:
    categ = "Sênior"
elif idade > 14:
    categ = "Júnior"
elif idade > 9:
    categ = "Mirim"
else:
    categ = "Infantil"
print(f"Classificação: {categ}.")
