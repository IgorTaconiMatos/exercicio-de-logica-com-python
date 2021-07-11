from time import sleep


def contador(inicio, fim, passo):
    print("-" * 30)
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print("-" * 30)
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=" ", flush=True)
            sleep(0.5)
            cont += passo
        print("Fim!")
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=" ", flush=True)
            sleep(0.5)
            cont -= passo
        print("Fim!")


contador(1, 10, 1)
contador(10, 0, 2)

print("-" * 30)
print("Agora é a sua vez de personalizar a contagem")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(inicio, fim, passo)
