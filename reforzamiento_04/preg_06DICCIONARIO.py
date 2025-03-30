"""Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario."""
val_1 = input("Ingrese el primer numero")
val_2 = input("Ingrese el segundo numero")
val_3 = input("Ingrese el tercer numero")
val_4 = input("Ingrese el cuarto unumero")
val_1 = int(val_1)
val_2 = int(val_2)
val_3 = int(val_3)
val_4 = int(val_4)
n1, n2, n3, n4 = val_1, val_2, val_3, val_4
dic = {}
dic[n1] = pow(n1,3)
dic[n2] = pow(n2,3)
dic[n3] = pow(n3,3)
dic[n4] = pow(n4,3)

print(dic)