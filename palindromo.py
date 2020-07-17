def palindromo(palabra):
  #Quitar los espacios
  #Reemplaza los espacios por caracter vacio
  palabra = palabra.replace(' ','')
  #todo a minusculas.
  palabra = palabra.lower()
  #nueva variable con la palabra invertida
  invertida = palabra[::-1]
  #La palabra se lee igual a invertida?
  if palabra == invertida:
    return True
  else:
    return False

def run():
  palabra = input('Ingresa una palabra: ')
  es_palindromo = palindromo(palabra)
  if es_palindromo == True:
    print('Es palindromo')
  else:
    print('No es palindromo')

#Entry point de un programa en Python es una buena practica
if __name__ == '__main__':
  run()

