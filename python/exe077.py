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
