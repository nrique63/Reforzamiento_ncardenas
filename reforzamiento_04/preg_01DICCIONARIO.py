"""Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal."""
dic1 = {"nombre": "Enrique", "edad": 18, "salario": 2000, "año de nacimiento": 2007}
print("El diccionario inicial es {}".format(dic1))

print(list(dic1))

valores = list(dic1.values())
print(valores)

listafinal = list(dic1) + valores
print(listafinal)