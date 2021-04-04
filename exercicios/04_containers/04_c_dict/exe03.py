"""
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
from datetime import date

dados = dict()

# criar chave "nome" e adicionar valor
dados["nome"] = str(input("Nome: ")).strip().capitalize()
# armazenar ano de nascimento
nasc = int(input("Ano de nascimento: "))
# criar chave "idade" e adicionar valor
dados["idade"] = date.today().year - nasc
# criar chave "ctps" e adicionar valor
dados["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))
# verificar condição
if dados["ctps"] > 0:
    # criar chave "contratação" e adicionat valor
    dados["contratação"] = int(input("Ano de contratação: "))
    # criar chave e adicionar valor
    dados["salário"] = float(input("Salário: R$"))
    # criar chave e adicionar valor
    dados["aposentadoria"] = dados["contratação"] + 35 - nasc

print(">" * 35)
# mostrar dados formatado
for k, v in dados.items():
    print(f"{k} tem valor {v}")
