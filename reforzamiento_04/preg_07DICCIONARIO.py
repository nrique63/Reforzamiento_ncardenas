"""Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso
y las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos. Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas."""
dic = {}   #solo para 2 alumnos
x = input("Indicar la cantidad de alumnos:")
a, b = input("Indicar nombres de alumnos:").split(",")
c, d = input("Indicar notas de alumnos respectivamente:").split(",")
c = int(c)
d = int(d)
dic[a] = c
dic[b] = d
print(dic)
print("El alumno {} tiene la nota de {}".format(a, c))
print("El alumno {} tiene la nota de {}".format(b, d))