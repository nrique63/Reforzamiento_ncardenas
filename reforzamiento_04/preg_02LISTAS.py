"""Crear un programa en Python donde tendrás una lista con 5 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista.
"""
departamentos = ["Lima","Loreto", "Ayacucho", "Ica", "Apurimac"]
dep1 = input("Ingrese el primer departamento :")
dep2 = input("Ingrese el segundo departamento :")
departamentos[1] = dep2
print(departamentos)