class Servidor:
  marca = "Dell"
  def __init__(self, system, ip):
    self.system = system
    self.ip = ip
    self.programs = []

  def __str__(self):
    return f"El servidor tiene un so: {self.system} y tiene una ip: {self.ip}"

  def install_program(self, program):
    self.programs.append(program)

server_1 = Servidor("Ubuntu", "10.0.0.23")
print(server_1)