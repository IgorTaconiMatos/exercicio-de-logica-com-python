salario = float(input("Qual o salário do seu funcionário: R$"))

if salario <= 1250:
    # calcular a porcentagem de 15%
    print(
        f"Quem ganhava R${salario} passa a ganhar R${salario + salario * 0.15:.2f} agora."
    )
else:
    # calcular a porcentagem de 10%
    print(
        f"Quem ganhava R${salario} passa a ganhar R${salario + salario * 0.1:.2f} agora."
    )
