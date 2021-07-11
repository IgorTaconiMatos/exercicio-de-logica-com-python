# armazenar informações
nome = str(input("Nome: ")).strip()
senha = str(input("Senha: ")).strip()

# enqunanto as informações forem iguais
while senha == nome:
    senha = str(input("Senha não pode ser igual ao nome.\nSenha: ")).strip()
# fim do programa
print("Informações registradas.")
