from random import randint

# gerar um número inteiro aleatório de 0 a 5
pensei = randint(0, 5)
print("–=–" * 15)
print("Vou pensar em um número entre 0 e 5.\nTente adivinhar.")
print("–=–" * 15)
# armazenar informação do usuário
num = int(input("Que número eu pensei? "))

# se maior que 5, faça...
if num > 5:
    print("Informação inválida")
# se diferente da variável pensei, faça...
elif num != pensei:
    print("Você ERROU!. Eu pensei no número {}".format(pensei))
# se igual a variável, faça...
else:
    print("ACERTOU!!. Eu pensei exatamente nesse número.\nMEUS PARABÉNS!!.")
