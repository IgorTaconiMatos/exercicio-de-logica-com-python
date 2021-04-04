"""
Faça um geradir de PA mostrando 10 termos. No final, pergunte para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
"""

from time import sleep

# variálvel de início e de parada
gerar = 3
novos = 3

print(
    """Gerandor de PA!!
[ 0 ] Encerrar programa
[ 1 ] Iniciar programa"""
)

# iniciar programa
gerar = int(input(">>>Qual sua opção? "))
# verificar "gerar"
if gerar == 1:
    # armazenar informações
    termo = int(input("Primeiro termo: "))
    razao = int(input("Razão da PA: "))
    # contador de termos e quantidade de termos
    cont = 0
    quant = 10

    # enquanto a opção do usuário for continuar
    while gerar != 0 and novos != 0:
        # loop de controle
        while cont < quant:
            print(termo, end=" ")
            # mostrar termos
            if cont < quant - 1:
                print("→", end=" ")
            else:
                print(".")
            # variável de controle
            cont += 1
            # termo conseguinte
            termo += razao
        sleep(0.5)
        # novos termos
        novos = int(
            input(
                "Digite 0 para finalizar\nOu informe quantos termos a mais você quer mostrar: "
            )
        )
        # gerar novos termos
        quant += novos
# encerrar
elif gerar == 0 or novos == 0:
    print("Processando informação")
    sleep(1)
# verificação de erro
else:
    print("Erro")
print(f"A prograssão foi finalizado com {cont} termos.")
