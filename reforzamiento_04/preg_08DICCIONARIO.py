""". Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”
"""
agenda = {}
a, b = (input("Ingresar nombres de alumnos:").split(","))
c, d = (input("Ingrese los numeros de las personas correspondientes:").split(","))
agenda[a] = c
agenda[b] = d
buscar = input("Ingrese el nombre que desea buscar")
valor = buscar in agenda.keys()
if valor == True:
    print("El nombre se encuentra en la agenda")
if valor == False:
    print("El nombre no se encuentra en la agenda")


print(agenda)