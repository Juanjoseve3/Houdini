# -*- coding: utf-8 -*-
"""Taller Recuperación Quiz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rPNi3VCkOrTEf6VXANnyxqCjiV_eM5LT
"""

def recorrer_caracol_horario(matriz):
  #Recorre la matriz desde la esquina superior izquierda en sentido horario
    if not matriz:
        return []

    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    inicio_fila = 0
    inicio_columna = 0
    fin_fila = filas - 1
    fin_columna = columnas - 1

    while inicio_fila <= fin_fila and inicio_columna <= fin_columna:
        for i in range(inicio_columna, fin_columna + 1):
            resultado.append(matriz[inicio_fila][i])

        for i in range(inicio_fila + 1, fin_fila + 1):
            resultado.append(matriz[i][fin_columna])

        if inicio_fila < fin_fila:
            for i in range(fin_columna - 1, inicio_columna - 1, -1):
                resultado.append(matriz[fin_fila][i])

        if inicio_columna < fin_columna:
            for i in range(fin_fila - 1, inicio_fila, -1):
                resultado.append(matriz[i][inicio_columna])

        inicio_fila += 1
        inicio_columna += 1
        fin_fila -= 1
        fin_columna -= 1

    return resultado

"""Iniciamos definiendo el método, en mi caso el recorrido_caracol.

- Tenemos en cuenta el que no exista una matriz retornando una lista vacía.

- Definimos las variables filas, columnas y resultado, siendo este último el que contendrá el resultado del recorrido de la matriz.

- Definimos las variables inicio_fila, inicio_columna, fin_fila y fin_columna, principalmente para orientarnos dentro de la matriz.

- Creamos un while que compara el tamaño del inicio con el fin, tanto de fila como de columna, esto dado que recibiremos una matriz de NxM y no podemos para el ciclo si hay más filas que columnas o viceversa.

  - El primer for hace un recorrido de la fila superior desde la columna inicial hasta la columna final + 1; el columna final + 1 se debe a que se debe incluir el elemento en la última posición de la fila superior.

  - El segundo for hace un recorrido de la columna derecha desde la fila inicial + 1 a la fila final + 1; el fila inicial + 1 se debe a que ya procesamos la primera fila en el ciclo anterior, y el fila final + 1 se debe a que se debe incluir el último elemento en la posiciónd de la columna derecha.

  - El tercer for hace un recorrido de la columna izquierda desde la columna final - 1 hasta la columna inicial - 1, y el tercer parametro del for que es -1 se debe a que vamos a recorrer la fila inferior de derecha a izquierda; el columna final - 1 se debe a que vamos a recorrer desde la penúltima columna, y el columna inicial - 1 se debe a que vamos a ejecutar el for esa cantidad de veces.

  - El cuarto for hace un recorrido de la fila inferior desde la fila final -1 hasta la fila inicial en pasos de -1, y el tercer parametro del for que es -1 se debe a que vamos a recorrer la columna izquierda de abajo hacia arriba; el fila final -1 se debe a que vamos a recorrer desde la penúltima fila.

- Después de cada for se actualizan las variables de inicio y fin de fila y columna. Incrementando inicio de fila y columna, y disminuyendo final de fila y columna. Se hace esto para evitar repetición de elementos.

- Para finalizar retornamos una la lista resultado que contiene los elementos que fuimos recorriendo de forma de caracol
"""

def recorrer_caracol_antihorario(matriz):
  #Recorre la matriz desde la esquina superior izquierda en sentido antihorario
    if not matriz:
        return []

    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    inicio_fila = 0
    inicio_columna = 0
    fin_fila = filas - 1
    fin_columna = columnas - 1

    while inicio_fila <= fin_fila and inicio_columna <= fin_columna:
        for i in range(inicio_fila, fin_fila + 1):
            resultado.append(matriz[i][inicio_columna])

        for i in range(inicio_columna + 1, fin_columna + 1):
            resultado.append(matriz[fin_fila][i])

        if inicio_fila < fin_fila:
            for i in range(fin_fila - 1, inicio_fila - 1, -1):
                resultado.append(matriz[i][fin_columna])

        if inicio_columna < fin_columna:
            for i in range(fin_columna - 1, inicio_columna, -1):
                resultado.append(matriz[inicio_fila][i])

        inicio_fila += 1
        inicio_columna += 1
        fin_fila -= 1
        fin_columna -= 1

    return resultado

"""Iniciamos definiendo el método, en mi caso el recorrido_caracol.

- Tenemos en cuenta el que no exista una matriz retornando una lista vacía.

- Definimos las variables filas, columnas y resultado, siendo este último el que contendrá el resultado del recorrido de la matriz.

- Definimos las variables inicio_fila, inicio_columna, fin_fila y fin_columna, principalmente para orientarnos dentro de la matriz.

- Creamos un while que compara el tamaño del inicio con el fin, tanto de fila como de columna, esto dado que recibiremos una matriz de NxM y no podemos para el ciclo si hay más filas que columnas o viceversa.

  - El primer for hace un recorrido de la fila superior desde la columna inicial a la columna final.

  - El segundo for hace un recorrido de la columba derecha desde la fila inicial + 1 hasta la fila final; el fila inicial + 1 se debe a que ya hemos tomado el primer elemento desde el for anterior.

  - El tercer for hace un recorrido de la fila inferior desde la columna final - 1 hasta la columna inicial; solo si la fila final es mayor a la inicial, esto se debe a como mencioné anteriormente recibimos una matriz NxM.

  - El cuarto for hace un recorrido de la columna izquierda desde la fila final -1 hasta la fila inicial + 1; solo si la columna final es mayor a la inicial, nuevamente, esto se debe a como mencioné anteriormente recibimos una matriz NxM.

- Después de cada for se actualizan las variables de inicio y fin de fila y columna. Incrementando inicio de fila y columna, y disminuyendo final de fila y columna. Se hace esto para evitar repetición de elementos.

- Para finalizar retornamos una la lista resultado que contiene los elementos que fuimos recorriendo de forma de caracol
"""

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
recorrer_caracol_horario(matriz)

matriz = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
recorrer_caracol_antihorario(matriz)

[[1, 2, 3,4],
 [5, 6, 7,8],
 [9,10,11,12],
 [13,14,15,16]]