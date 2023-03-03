inventario = {"Ubuntu" : 100, "Amazon Linux" : 500, "Debian" : 1000, "Arch" : 50}

print(inventario)

#si el valor no existe lanza una excepcion
# print(inventario["Linux"])

#con get no ocurre esto
inventario.get("Linux")

#cambio de valor a una llave
inventario["Debian"] = 34

#si no existe la asignacion la crea
inventario["Red Hat"] = 80

print(inventario)

#eliminar una llave del diccionario, si no se le pasa ningun argumento elimina la ultima llave
inventario.pop("Ubuntu")

print(inventario)

#keys devuelve los nombres de las llaves del diccionario
#list convierte a lista lo que se le pase por parametro
print(list(inventario.keys))

#values devuelve los valores de las llaves del diccionario
print(list(inventario.values))

