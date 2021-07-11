aluno = {}

# armazenar chave "Nome" e adicionar valor
aluno["Nome"] = str(input("Nome: ")).strip().capitalize()
# armazenar chave "Média"' e adicionar valor
aluno["Média"] = float(input(f'Média de {aluno["Nome"]}: '))

# cria chave "Situação" e adicionar valor dependendo do valot da chave "Média"
if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
elif aluno["Média"] >= 5:
    aluno["Situação"] = "Recuperação"
else:
    aluno["Situação"] = "Reprovado"

# mostrar informações
for k, v in aluno.items():
    print(f"{k} é igual a {v}")
