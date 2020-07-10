menu = """
Bienvenido a mi conversor de monedas 💵

1 - Pesos Mexicanos
2 - Pesos Colombianos
3 - Pesos Argentinos

Elige una opcion: """
opcion = input(menu)

if opcion == '1':
  pesos = input("¿Cuantos pesos MXN tienes?: ")
  pesos = float(pesos)
  valor_dolar =22.70
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes $ " + dolares + " dolares" )
elif opcion =='2':
  pesos = input("¿Cuantos pesos Colombianos tienes?: ")
  pesos = float(pesos)
  valor_dolar =3623.45
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes $ " + dolares + " dolares" )
elif opcion =='3':
  pesos = input("¿Cuantos pesos Argentinos tenés?: ")
  pesos = float(pesos)
  valor_dolar =70.88
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes $ " + dolares + " dolares" )
else:
  print("No valida, elige una opcion correcta por favor: ")