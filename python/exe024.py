# armazenar segmentos
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

# formula para verificar se pode ser formado uma triângulo
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima podem formar um triângulo", end=" ")
    # verificar a classificação do triângulo
    if a == b == c:
        print("EQUILÁTERO")
    elif a == b or a == c or b == c:
        print("ISÓCELES")
    elif a != b != c:
        print("ESCALENO")
else:
    print("Não pode ser formado um triângulo.")
