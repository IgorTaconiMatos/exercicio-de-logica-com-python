def escada(n):
    for degral in range(1, n + 1):
        for cada in range(0, degral):
            print(f"{degral:2}", end=" ")
        print("")


escada(10)
