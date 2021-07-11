def valor_pagamento(valor, dias):
    if dias == 0:
        return valor
    else:
        juros_dia = dias * 0.001
        multa = valor * 0.03
        valor += multa + juros_dia
        return valor


quant = total = 0

while True:
    valor_prestacao = float(input("Valor da prestação. (0 para encerrar) R$"))
    if valor_prestacao == 0:
        break
    dias_atraso = int(input("Dias de atraso. "))

    novo_valor = valor_pagamento(valor_prestacao, dias_atraso)
    print(f"Você tem que pagar R${novo_valor:.2f}")
    total += novo_valor
    quant += 1

print("—" * 40)
print(f"Foram realizados {quant} pagamentos no valor total de R${total:.2f}.")
