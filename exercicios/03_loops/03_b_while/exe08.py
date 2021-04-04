"""
Leia o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

# armazenar informações
termo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
# contador
cont = 0

# inicio do loop com condição
while cont < 10:
    # mostrar termos
    print(termo, end=" ")
    if cont < 9:
        print("→", end=" ")
    else:
        print("", end=" ")
    # modificar condição
    cont += 1
    # adicionar a razão ao termo
    termo += razao
