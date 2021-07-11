print("=" * 40)
print(f'{"BANCO WTF": ^35}')
print("=" * 40)

valor = int(input("Qual o valor você quer sacar? R$"))

duzentos = cem = cinquenta = vinte = dez = cinco = um = 0
while valor >= 200:
    valor -= 200
    duzentos += 1
while valor >= 100:
    valor -= 100
    cem += 1
while valor >= 50:
    valor -= 50
    cinquenta += 1
while valor >= 20:
    valor -= 20
    vinte += 1
while valor >= 10:
    valor -= 10
    dez += 1
while valor >= 5:
    valor -= 5
    cinco += 1
while valor >= 1:
    valor -= 1
    um += 1

print("=" * 40)
if duzentos > 0:
    print(f"Total de {duzentos} células de R$200")
if cem > 0:
    print(f"Total de {cem} células de R$100")
if cinquenta > 0:
    print(f"Total de {cinquenta} células de R$50")
if vinte > 0:
    print(f"Total de {vinte} células de R$20")
if dez > 0:
    print(f"Total de {dez} células de R$10")
if cinco > 0:
    print(f"Total de {cinco} células de R$5")
if um > 0:
    print(f"Total de {um} células de R$1")
print("Obrigado por usar o WTF")
