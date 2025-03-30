"""Escribir un programa donde ingresarás el tamaño de la lista mediante
consola, este tamaño servirá para ingresar una cantidad X de nombres de
alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de
la lista que fueron ingresados."""
cant = input("Ingrese la cantidad de valores de la lista : ")
cant = int(cant)
valores  = input("Añada los nombres a la lista : ").split(",")
lista = []
lista.append(valores)
print("El tamaño de la lista es de : {}".format(cant))
print("La lista con los nombres es : {}".format(lista))


