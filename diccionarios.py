def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])
    poblacion_paises = {
        'Argentina': 44938712,
        'Brasil': 210147125,
        'Colombia': 50372424,
    }

    # print(poblacion_paises['Argentina'])
    # print(poblacion_paises['Mexico'])

    # Recorrer el Diccionario
    # Metodo .keys() : Devuelve las llaves.
    # for pais in poblacion_paises.keys():
    #     print(pais)

  # Metodo .values() : Develve los valores de las llaves.
    # for pais in poblacion_paises.values():
    #     print(pais)

    # Metodo .item() : Devuelve el Item completo: Key & value
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' tiene ' + str(poblacion) + ' Habitantes')


if __name__ == '__main__':
    run()
