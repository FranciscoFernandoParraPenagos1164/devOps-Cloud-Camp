class User:
  def __init__(self, nombre, edad, ubicacion, correo):
    self.nombre = nombre
    self.edad = edad
    self.ubicacion = ubicacion
    self.correo = correo

  def __str__(self):
    return f"Usuario con nombre: {self.nombre} Ubicado en {self.ubicacion} y con correo {self.correo}"

class Student(User):
  def __init__(self, nombre, edad, ubicacion, correo):
    super().__init__(nombre, edad, ubicacion, correo)

class Teacher(User):
  def set_modules(self, modulos):
    self.modulos = modulos

class Course:
  def __init__(self, nombre, profesor, lista_estudiantes):
    self.nombre = nombre
    self.profesor = profesor
    self.lista_estudiantes = lista_estudiantes
  
  def __str__(self):
    return f"el curso {self.nombre} con el profesor {self.profesor.nombre} tiene {len(self.lista_estudiantes)}"

  def add_student(self, estudiante):
    self.lista_estudiantes.append(estudiante)

pablo = Student("Pablo Peralta", 40, "Colombia", "pablo.peralta@gmail.com")
pedro = Student("Pedro Perez", 35, "Peru", "pedro.perez@gmail.com")
albert = Teacher("Albert Ramirez", 38, "Colombia", "albert.ramirez@gmail.com")
curso_python = Course("Introduccion a python", albert, [pablo, pedro])

lina = Student("Lina Perez", 35, "Peru", "lina.perez@gmail.com")