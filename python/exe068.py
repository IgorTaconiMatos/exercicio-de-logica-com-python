# armazenar a informação
expr = input("Digite sua expressão: ")
# se a quantidade de '(' for igual a quantidade de ')'
if expr.count("(") == expr.count(")"):
    print("Sua expressão é válida")
# se não
else:
    print("Sua expressão não é válida")
