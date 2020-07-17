
def conversor(tipo_pesos, valor_dolar):
  pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
  pesos = float(pesos)
  dolares = pesos / valor_dolar
  dolares = round(dolares, 2)
  dolares = str(dolares)
  print("Tienes $ " + dolares + " dolares" )  

menu = """
Bienvenido a mi conversor de monedas 💵

1 - Pesos Mexicanos
2 - Pesos Colombianos
3 - Pesos Argentinos

Elige una opcion: """

opcion = input(menu)

if opcion == '1':
 conversor("Mexicanos",22.72)
elif opcion =='2':
  conversor("Colombianos", 3623.45)
elif opcion =='3':
  conversor("Argentinos", 70.88)
else:
  print("No valida, elige una opcion correcta por favor: ")