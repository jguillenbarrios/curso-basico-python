def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(0, 10000):
    #     print(i)
    #     if i == 5865:
    #         break
    texto = input('Escribe un texto cualquiera: ')
    for letra in texto:
        if letra.upper() == 'O':
            break

        print(letra.upper())


if __name__ == '__main__':
    run()
