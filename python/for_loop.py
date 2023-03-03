linux = ["Ubuntu", "Amazon linux", "Debian", "Arch"]

for server in linux:
  print(server)

  if server == "Debian":
    print("Me gusta Debian")
    
inventario = {"Ubuntu" : 100, "Amazon Linux" : 500, "Debian" : 1000, "Arch" : 50}
print("\n")

for server in inventario:
  print(server)
print("\n")

for letra in "mi string":
  print(letra)
print("\n")

listas_puntos = [(1, 2), (2, 3), (3, 4)]

for x, y in listas_puntos:
  print("x : " + str(x))
  print("y : " + str(y))
print("\n")

for server, amount in inventario.items():
  print("OS : " + server)
  print("cantidad : " + str(amount))
print("\n")

for number in range(100):
  print(number)
