"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

#armazenar informações
nome = str(input('Nome: ')).strip()
senha = str(input('Senha: ')).strip()

#enqunanto as informações forem iguais
while senha == nome:
	senha = str(input('Senha não pode ser igual ao nome.\nSenha: ')).strip()
#fim do programa
print('Informações registradas.')
