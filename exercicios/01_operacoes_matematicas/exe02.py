"""
Construir um programa que efetue o cálculo do salário líquido de um professor. Para fazer este programa, você deverá possuir alguns dados, tais como: valor da hora aula, número de horas trabalhadas no mês e percentual de desconto do INSS. Em primeiro lugar, você deve estabelecer qual será o seu salário bruto para efetuar o desconto a ter o valor do salário líquido.
"""

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
