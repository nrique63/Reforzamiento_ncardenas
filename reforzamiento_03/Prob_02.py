cursos = ["desarrollo personal y liderazgo","redaccion", "calculo", "calculo", "calculo", "medio ambiente",
          "algebra y geometria analitica", "programacion"]
print("La lista de cursos es {}".format(cursos))
print("La cantidad de veces que se repite el curso de calculo es de {} veces".format(cursos.count("calculo")))
cursos.pop(1)
print("La lista de cursos actualizada es {}".format(cursos))