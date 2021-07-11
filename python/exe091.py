def fizzbuzz(n):
    for num in range(1, n + 1):
        if not num % 15:
            print("fizzbuzz")
        elif not num % 3:
            print("fizz")
        elif not num % 5:
            print("buzz")
        else:
            print(num)


valor = int(input("Informe o fim da contagem: "))
fizzbuzz(valor)
