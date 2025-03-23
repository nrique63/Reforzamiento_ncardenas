basesdt = ["ORACLE", "MYSQL", "POSTGRESQL", "MARIADB","MYSQL", "SQLSERVER", "ORACLE",
           "Microsoft SQL Server", "POSTGRESQL", "IBM DB2", "POSTGRESQL"]
print(basesdt.count("ORACLE"))
print("La cantidad de veces que se repite ORACLE es : {}".format(basesdt.count(basesdt[0])))
print(basesdt.count("MYSQL"))
print("La cantidad de veces que se repite MYSQL es : {}".format(basesdt.count(basesdt[1])))
print(basesdt.count("POSTGRESQL"))
print("La cantidad de veces que se repite POSTGRESQL es : {}".format(basesdt.count(basesdt[2])))