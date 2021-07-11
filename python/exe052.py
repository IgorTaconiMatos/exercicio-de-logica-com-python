while True:
    num = int(input("Quer ver a tabuada de qual valor? "))
    if num < 0:
        break
    for tab in range(1, 11):
        print(f"{num} x {tab:2} = {num * tab:2}")
print("PROGRAMA TABUADA ENCERRADO. Volte sempre.")
