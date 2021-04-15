km = float(input("Quantos Km rodados? "))
dias = int(input("Quantos dias alugados? "))
total = dias * 60 + km * 0.15

print(f"O total a pagar é de R${total:.2f}.")
