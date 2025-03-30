"""Crear un diccionario con 6 departamentos en el país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.
- Comprobar que no existe este departamento borrado dentro del
diccionario.
"""
departamentos = {'dep1':"Lima", 'dep2':'Ancash', 'dep3':'Cusco', 'dep4':'Puno', 'dep5':'Junin', 'dep6':'La Libertad'}
print("El diccionario inicial es :{}".format(departamentos))
del departamentos['dep1']
departamentos['dep5'] = "Madre de Dios"
if 'Junin' in departamentos:
    print("El departamento Junin se encuentra en el diccionario")
if 'Junin' not in departamentos:
    print("El departamentos Junin ya  no se encuentra en el diccionario")

print(departamentos)
