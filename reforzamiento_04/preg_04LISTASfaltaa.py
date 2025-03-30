"""4. Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de
TI) y harás una copia donde adrede agregarás nombres que estarán
repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también la lista inicial"""
tamaño = input("Ingrese el tamaño de la lista:")
print("Ingrese el nombre de 5 compañias relacionadas con el mundo de TI")
var_01 = input()
var_02 = input()
var_03 = input()
var_04 = input()
var_05 = input()
list = []
a, b, c, d, e = var_01, var_02, var_03, var_04, var_05
list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)

copias = input("Agrege nuevos nombres a la lista")
if copias in list:
    list2 = list.copy()
    list2.remove(copias)
    print("La lista sin los elementos repetidos es :{}".format(list2))

print("La lista inicial era:", list)


