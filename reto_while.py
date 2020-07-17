def run():
    texto = input('Escribe algo... (para salir escribe q): ')
    while not texto.strip() == 'q':
        texto = input('Sigue: ')


if __name__ == '__main__':
    run()
