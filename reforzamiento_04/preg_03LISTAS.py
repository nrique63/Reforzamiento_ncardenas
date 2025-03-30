"""Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y esta será agregada a la lista.
 Finalmente mostrar la lista actualizada en consola"""
nombres = ["Alvaro", "Frank", "Jorge", "Estefano", "Enrique"]
nuevo = input("Ingrese un nombre: ")
valor = nuevo in nombres


if valor == False:
    print("El nombre {} no se encuentra en la lista".format(nuevo))
    nombres.append(nuevo)
if valor == True:
    nombres.remove(nuevo)

print(nombres)


