def hello_world(languaje):
  #upper convierte todos los caracteres a mayuscula
  if languaje == "es":
    return "Hola mundo".upper()
  elif languaje == "en":
    return "Hello world".upper()
  print("Hello world".upper())

def congratulations(nombre, edad):
  print("Hola" + nombre + "\nfeliz cumpleaños numero " + edad)

# print(hello_world("es"))
# print(hello_world("en"))
# print(hello_world("es"))
congratulations("Francisco", "18")

