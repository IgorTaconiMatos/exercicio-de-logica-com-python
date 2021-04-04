"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

números = []

# iniciar o loop no intervalo de 0 a 4
for valor in range(0, 5):
    # armazenar números
    num = int(input("Digite um valor: "))
    # se for o primeiro loop ou "num" for maior que o último número da lista
    if valor == 0 or num > números[-1]:
        # adicionar ao final da lista
        números.append(num)
        print("Valor adicionado ao final da lista.")
    # senão for
    else:
        # verificar valores da lista
        for índice, valor in enumerate(números):
            # se número for menor que valor
            if num < valor:
                # inserir número na posição do valor
                números.insert(índice, num)
                print(f"Número adicionado na posição {índice}")
                break

# mostrar os valores
print("Os valores informados foram:", end=" ")
for val in números:
    print(val, end=" ")
