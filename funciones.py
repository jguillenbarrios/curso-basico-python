# def imprimir_mensaje():
#   print("Mensaje especial: ")
#   print("Estoy aprendiendo a usar funciones")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def saludo(mensaje):
  
  print("hola")
  print("Como estas")
  print(mensaje)
  print("adios")


opcion = input("Elig euna opcion (1, 2, 3): ")
if opcion =='1':
  saludo("Elegiste la opcion 1")
elif opcion=='2':
  saludo("Elegiste la opcion 2")
elif opcion=='3':
  saludo("Elegiste la opcion 33")
else:
  print("Elige la opcion correcta")