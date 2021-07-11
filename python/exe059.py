from random import randint

# gerar 5 valores aleatótio dentro de uma tupla
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print("Os valores sorteados foram: ", end="")
# varrer a tupla
for n in range(0, 5):
    # mostrar os valores sorteados
    print(num[n], end=" ")
# mostrar o maior e o menor índice na tupla
print(f"\nO maior é {max(num)} e o menor é {min(num)}")
