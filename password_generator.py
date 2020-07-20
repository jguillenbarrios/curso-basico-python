# modulos
import random


def generate_password():

  # Creamos diferentes listas
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                  'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    minusculas = minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                               'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                               'u', 'v', 'w', 'x', 'y', 'z']
    simbolos = ['!', '#', '$', '&', '/', '(', ')']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # Sumamos las listas, ahora tenemos una lista con TODOS los diferentes caracteres.
    caracteres = mayusculas + minusculas + simbolos + numeros
    # Genramos una lista vacia
    contrasena = []
    # recorremos la lista N veces (15) para generar una contraseña
    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)
    # Esto genera un String de una lista.
    contrasena = "".join(contrasena)
    return contrasena


def run():
    password = generate_password()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()
