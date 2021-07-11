# tupla com as informações
bras = (
    "Internacional",
    "Flamengo",
    "Atlético-MG",
    "Fluminese",
    "São Paulo",
    "Santos",
    "Palmeiras",
    "Grêmio",
    "Sport",
    "Fortaleza",
    "Corinthians",
    "Ceará",
    "Atlético-GO",
    "Botafogo",
    "Bahia",
    "Vasco",
    "Coritiba",
    "Bragantino",
    "Athletico-PR",
    "Goiás",
)

print("-=" * 20)
# mostras a tupla
print(f"Lista de times do Brasileirão: {bras}")
print("-=" * 20)
# mostrar os 5 primeiros
print(f"Os 5 primeiros são {bras[:6]}")
print("-=" * 20)
# mostrar os 4 últimos
print(f"Os 4 últimos são {bras[:15:-1]}")
print("-=" * 20)
# mostrar em ordem alfabética
print(f"Times em ordem alfabética: {sorted(bras)}")
print("-=" * 20)
# procurar o índice "Sport" na tupla
print("O Sport está na {} posição".format(bras.index("Sport")))
