"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

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
