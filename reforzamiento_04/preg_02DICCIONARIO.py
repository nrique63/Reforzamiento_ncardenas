"""Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado.
"""
dic1 = {"nombre": "Enrique", "edad": 18, "salario": 2000, "año de nacimiento": 2007}
print("La lista inicial es :{}".format(dic1))
dic1['dni'] = 70633721
print("El salario es {}".format(dic1['salario']))
print("El dni es {}".format(dic1['dni']))
del dic1['edad']
print(dic1)