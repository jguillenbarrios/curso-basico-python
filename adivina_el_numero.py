# Modulos
import random

# Funcion Principal


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_usuario = int(input('Elige un numero del 1 al 100: '))
    while numero_usuario != numero_aleatorio:
        if numero_usuario < numero_aleatorio:
            print(' Busca un numero mas grande ;) ')
        else:
            print(' Busca un numero mas pequeño ;) ')
        numero_usuario = int(input("Elige otro numero...: "))
    print('GANASTE!')


# Entry point
if __name__ == '__main__':
    run()
