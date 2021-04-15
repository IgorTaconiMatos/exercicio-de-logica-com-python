valor_hora = float(input("Valor hora/aula: R$"))
horas_trab = float(input("Horas trabalhadas: "))
perc_desc = float(input("Percentual de desconto: "))
print(perc_desc)
salar_bruto = valor_hora * horas_trab
salar_liquido = salar_bruto * (salar_bruto / 100)

print(
    f"""O salário bruto será R${salar_bruto:.2f}.
Com o desconto de {perc_desc}%, o salário líquido será R${salar_liquido:.2f}"""
)
