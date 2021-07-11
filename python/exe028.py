from time import sleep

# a variavel 'i' irá varrer de 10 a 0 partindo do 10
for contagem in range(10, 0, -1):
    # escrever a variavel no presente momento
    print(contagem)
    # parar por 1 segundo
    sleep(1)
print("BUM! " * 3)
