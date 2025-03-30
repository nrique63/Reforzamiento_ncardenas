"""Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”
Considerar que cada vez que se realice algún pago o ingreso de una nueva
factura se mostrará inmediatamente al diccionario actualizado"""
facturas = {"00052":2000,}
var_1 = input("¿Que proceso desea realizar?")
if var_1 == "pedir":
    nfactura1 = input("Ingrese el numero de la factura")
    vfactura1 = input("Ingrese el valor de la factura")
    facturas[nfactura1] = vfactura1
    print("El nuevo diccionario es:{}".format(facturas))
if var_1 == "pagar":
    buscar = input("Cual es el numero de la factura?")
    valor = buscar in facturas.keys()
    if valor == True:
        print("La factura ya esta cancelada")
        del facturas[buscar]
        print("El nuevo diccionario es:{}".format(facturas))
    if valor == False:
        print("El número de  factura no existe")
        print("El nuevo diccionario es:{}".format(facturas))

#facturas[nfactura1] = vfactura1
