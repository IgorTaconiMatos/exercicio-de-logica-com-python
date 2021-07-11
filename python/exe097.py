def minera(base_dados):
    meio_diamante = list()
    diamantes_quantidade = 0
    for dado in base_dados:
        if dado == '<':
            meio_diamante.append(dado)
        elif dado == '>' and meio_diamante:
            meio_diamante.pop()
            diamantes_quantidade += 1

    return diamantes_quantidade


N = int(input())
for i in range(N):
    X = input()
    Y = minera(X)
    print(Y)
