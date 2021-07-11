def triangulo(a, b, c):
    if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
        return tipoTriangulo(a, b, c)
    return False


def tipoTriangulo(a, b, c):
    if a == b == c:
        tipo = "equilátero"
    elif a == b != c or c == b != a or c == a != b:
        tipo = "isósceles"
    elif a != b != c:
        tipo = "escaleno"
    else:
        tipo = "erro"
    return tipo


lado1 = int(input("Primeiro lado: "))
lado2 = int(input("Segundo lado: "))
lado3 = int(input("Terceiro lado: "))

verifica = triangulo(lado1, lado2, lado3)
if verifica is False:
    print("Os lados informados não podem formar um triângulo.")
else:
    print(f"Os lados informados formar um triângulo {verifica}.")
