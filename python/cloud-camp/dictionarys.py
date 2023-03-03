
# Estudiantes
# Los estudiantes los definimos como:
#{nombre: String, edad: number, ubicacion: String, correo: String}
francisco = {"nombre": "Francisco Parra", "edad": 18, "ubicacion": "Colombia", "correo": "franciscoticopp@gmail.com"}

#profesores
# {nombre: String, edad: number, ubicacion: String, correo: "", modulos: String[]}

def crate_course(profesor, estudiantes, tema):
  return {"profesor": profesor, "estudiantes": estudiantes, "tema": tema}