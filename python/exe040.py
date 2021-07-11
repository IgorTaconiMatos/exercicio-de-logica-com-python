from random import randint

quant_palpite = 0
# armazenar número do computador
computador = randint(1, 10)

print("Vou pensar em um número de 1 a 10.")
# armazenar informação
palpite = int(input("Tente adivinhar: "))
# somar quantidade de palpites
quant_palpite += 1
# criar um loop até acertar
while palpite != computador:
    print(f"Você errou. Eu pensei no número {computador}.")
    # armazenar informação
    palpite = int(input("Tente de novo: "))
    # somar quantidade de palpites
    quant_palpite += 1
    # armazenar número do computador
    computador = randint(1, 10)
print(">" * 30)
print(
    f"Você acertou. Eu pensei exatamente no número {palpite}.\nVocê deu {quant_palpite} palpites"
)
