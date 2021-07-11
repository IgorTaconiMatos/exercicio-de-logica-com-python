from datetime import date

ano = int(input("Digite o seu ano de nascimento: "))
# calcular idade
idade = date.today().year - ano
print(f"Você tem {idade} anos de idade.")

# fazer verificações.
if idade < 18:
    print(f"Faltam {18 - idade} ano(s) para você se alistar no serviço militar.")
elif idade == 18:
    print("Chegou a hora. Procure a junta de Serviço Militar mais próxima de você")
else:
    print(
        f"Já se passaram {idade - 18} anos do prazo de alistamento. Se você não vez o alistamento, regularize essa situação"
    )
