# -*- coding: utf-8 -*-
"""algoritmos_materia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15rJboQSlQGSBoqSG_vmAIm1vK1y4LGi4

### 3 metodos (crea matriz, muestra matriz, suma componentes matriz)
"""

import random
import numpy as np

def crear_matriz(n):   #0(n^2)
  matriz = []          #0(1)
  for i in range(n):   #0(n)
    matriz.append([])  #0(n)
    for j in range(n): #0(n^2)
      matriz[i].append(random.randint(0,10))   #0(n^2)
  return matriz        #0(1)

def mostrar_matriz(matriz):
  for i in(matriz):
    print(i)    #0(1)              #0(1)

def sumatoria(matriz):         #0(n)
  c = 0                        #0(1)
  for i in range(len(matriz)): #0(n)
   a = sum(matriz[i])          #0(n)
   c += a                      #0(n)
  return c                     #0(1)
  
matrix = crear_matriz(3) #0(1)
mostrar_matriz(matrix)
sumatoria(matrix)

"""#### Mismo codigo con menos lineas """

import random
def crear_matriz(n, matriz = []):  
  for i in range(n):
    matriz.append([])
    for j in range(n): (matriz[i].append(random.randint(0,10)))
  return matriz
def mostrar_matriz(matriz): (print(matriz))
def sumatoria(matriz, c = 0):
  for i in range(len(matriz)):a = sum(matriz[i]);c += a
  return c
sumatoria(crear_matriz(3))

"""# Inico de taller"""

# Matrices de referencia NxM y  NxN

matriz = [[1,2],
          [3,4],
          [5,6]]

matriz2 = [[1,2,3],
           [4,5,6]]

matriz3 = [[9,8],
           [7,6],
           [5,4],
           [3,2]]

matriz4 = [[12, 23, 3], 
          [44, 65, 62], 
          [74, 98, 95]]

"""## Punto 1
### Matriz con recorrido vertical(alternado)
"""

def recorridoVerticalMatriz(matriz): ### O(n^2)
  columns = len(matriz[0])           #O(1)
  i = 0                              #O(1)
  while i != columns:                #O(n)
    columna = [fila[i] for fila in matriz]  #O(n^2)
    if (i%2) != 0:                          #O(n)
      print(columna[::-1])                  #O(n)
    else:                                   #O(n)
      print(columna)                        #O(n)
    i += 1                                  #O(n)
    
### 2O(1) + 6O(n) + O(n^2) => O(n^2)  

recorridoVerticalMatriz(matriz3)  #O(n^2)

"""## Punto #2

### Matriz con recorrido zig-zag (No recursivo)
"""

def recorridoDiagonalMatriz(matriz):  #O(n^2)
  diagonalNormal = (len(matriz) - 1)*(-1)  #O(1)            #Voy a crear dos variables, una que lleve el conteo de las diagonales en zigzag ascedente y otra que lleve el conteo descendente
  diagonalInvertida = len(matriz) - 2      #O(1)             #Normal = Ascendente, Invertida = Descendente. normal siempre quedara con la cantidad de filas que haya en la matriz menos 1, luego lo convierto en negativo, esto para empiece desde matriz[0][0] y lo mismo hago con invertido pero le resto 2 y NO lo convierto negativo, asi toma la segunda diagonal.
  listaNum = []                            #O(1)             #Creo una lista donde voy a ir almacenando los numeros que vaya agarrando mientras recorre la matriz
  
  if(len(matriz) == 1):                    #O(1)             #En caso de que la  matriz se de 1x1  (Todo se explica en las matrices 3x3 en adelante, leer abajo primero)
    a = np.flipud(matriz).diagonal()       #O(1)
    listaNum.append(a)                     #O(1)

  if(len(matriz) == 2):                    #O(1)             #En caso de que la  matriz se de 2x2
    a = np.flipud(matriz).diagonal(-1)     #O(1)
    b = np.fliplr(matriz).diagonal()       #O(1)
    c = np.flipud(matriz).diagonal(1)      #O(1)
    listaNum.append(a), listaNum.append(b), listaNum.append(c)     #O(1)

  else:                                                  #O(1)
    for i in range(len(matriz)):                         #O(n)  #Ciclo con alcance hasta el numero de filas de la matriz 
      a = np.flipud(matriz).diagonal(diagonalNormal)     #O(n)  #guardo en dos variables las diagonales, en a iran las ascendentes y b las decendentes
      b = np.fliplr(matriz).diagonal(diagonalInvertida)  #O(n)  #esto debido a los metodos de las librerias que sque de numpy que funcionan entregandome las diagonales de acuerdo a como se las pidamos, observen que son dos metodos 
      listaNum.append(a)                                 #O(n)  #Agrego a la lista la primera diagonal 
      if b.size > 0:                                     #O(n)  #Aquí pregunto si b tiene algun elemento debido a que en la última iteración siempre estara vacía, con este condicional lo controlo
        listaNum.append(b)                               #O(n)  #Agrego a la lista la segunda diagonal 
      diagonalNormal += 2                                #O(n)  #Le agrego para que al volver a iniciar el ciclo inicie desde la diagonal donde se encuentra + 2
      diagonalInvertida -= 2                             #O(n)  #Lo mismo que arriba pero - 2, debido como funciona los metodos de numpy                          
      fixed = [list(arr) for arr in listaNum]            #O(n)  #Cada arreglo se vuelve una lista

  return fixed                                           #O(1)  #Retorno la lista con los valores ya organizados

#Suma del Big-O: 13O(1) + 9O(n) => 9O(n)

recorridoDiagonalMatriz(matriz4)  #O(1)

"""### Matriz con recorrido zig-zag (Recursivo)"""

def recorridoDiagonalMatrizRecursivo(matriz, diagonalNormal=0, diagonalInvertida=0, listaNum=[], c=0):    #O(n)
                                          
  if(len(matriz) == 1):                                         #O(n)
    a = np.flipud(matriz).diagonal()                            #O(n)
    listaNum.append(a)                                          #O(n)

  if(len(matriz) == 2):                                         #O(n)
    a = np.flipud(matriz).diagonal(-1)                          #O(n)
    b = np.fliplr(matriz).diagonal()                            #O(n)
    c = np.flipud(matriz).diagonal(1)                           #O(n)
    listaNum.append(a), listaNum.append(b), listaNum.append(c)  #O(n)

  else:                                                         #O(n)
    if(c == len(matriz)):                                       #O(n)
      return listaNum                                           #O(n)
    else:                                                       #O(n)
      if(c == 0):                                               #O(n)
        diagonalNormal = (len(matriz) - 1)*(-1)                 #O(n)
        diagonalInvertida = len(matriz) - 2                     #O(n)
      a = np.flipud(matriz).diagonal(diagonalNormal)            #O(n)
      b = np.fliplr(matriz).diagonal(diagonalInvertida)         #O(n)
      listaNum.append(a)                                        #O(n)
      if b.size > 0:                                            #O(n)
        listaNum.append(b)                                      #O(n)             
      fixed = [list(arr) for arr in listaNum]                   #O(n)

      return recorridoDiagonalMatrizRecursivo(matriz, diagonalNormal + 2, diagonalInvertida - 2, fixed, c + 1 )   #O(n)

#Suma del Big-O: 22O(n) => 22O(n)

recorridoDiagonalMatrizRecursivo(matriz4)   #O(1)

"""# A partir de aquí son los análisis y pruebas que realizamos para encontrar las soluciones

"""





"""### Metodo que nuestra los indices en forma vertical alternada (como determina el taller)"""

# Matriz nxn

for i in range(len(matrix)):
  columna = [fila[i] for fila in matrix]
  if (i%2) != 0 :
    print(columna[::-1])
  else:
    print(columna)

"""## Testeo

### Todo de aquí para abajo no va en el trabajo, solo es para probar cositas B)
"""

for i in range(len(matriz2)):
  columna = [fila[i] for fila in matriz2]
  if (i%2) != 0 :
    print(columna[::-1])
  else:
    print(columna)

print(matrix)
zzz= []
for i in range(len(matrix)):
  for j in range(len(matrix)):
    if (i%2) != 0 :
      zzz.append(matrix[i][j])
      print(matrix[i][j])
    else:
      zzz.append(matrix[i][j])
      print(matrix[i][j])
    
print(zzz)

cantSubList = len(matriz[i])
if cantSubList < 0:
  for i in range(len(matriz)):
    columna = [fila[i] for fila in matriz]
    if i % 2 != 0 :
        print(columna[::-1])
    else:
        print(columna)
        i += 1
else:
      print("hola")

"""ESOOOO CHECHOOOOOO  (Luego organizo lo que hicimos hoy)

A partir de aquí son pruebas del segundo ejercicio
---
Att: Severino
"""

matrix = [[1,2,7],
          [3,4,8],
          [5,6,9]]

matriz2 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matriz3 = [[9,8,3],
           [7,6,1],
           [5,4,2]]

#matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

dimension = len(matriz)

zigzag = True
for k in range(2 * dimension - 1):
    if zigzag:
        i = min(k, dimension - 1)
        j = k - i
    else:
        j = min(k, dimension - 1)
        i = k - j
    
    while i >= 0 and j < dimension:
        print(matriz[i][j])
        i -= 1
        j += 1
        
    zigzag = not zigzag

#matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

zigzag = True #Creo una bandera

for k in range(len(matriz) + len(matriz[0]) - 1): #Hago un bucle que itera entre 
#la suma de la longitud de la matriz y la longitud de la primera lista - 1
    if zigzag: #Si la bandera es True entonces se definen dos variables
        i = min(k, len(matriz) - 1) #i será el número mínnimo entre k y la longitud de la matriz - 1
        j = k - i #j será la diferencia entre k e i
    else:
        j = min(k, len(matriz[0]) - 1) #i será el número mínnimo entre k y la longitud de la matriz - 1
        i = k - j #i será la diferencia entre k e i
    
    while i >= 0 and j < len(matriz[0]): #Hago otro bucle donde comparo que i sea mayor o igual a 0 y además
    #que j sea menor que la longitud de la primera lista
        print(matriz[i][j], end=" ")
        i -= 1
        j += 1
        
    zigzag = not zigzag

zigzag = True 

for k in range(len(matriz) + len(matriz[0]) - 1):
    if zigzag:
      if k == len(matriz) -1:
        i = (min(k, len(matriz) - 1) ) -1
        j = (k - i) -1 
      else:
        i = min(k, len(matriz) - 1) 
        j = k - i 
    else:
        j = min(k, len(matriz[0]) - 1) 
        i = k - j
    
    while i >= 0 and j < len(matriz[0]): 
        print(matriz[i][j], end=" ")
        i -= 1
        j += 1
        
    zigzag = not zigzag

#matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

i = 0
j = 0
n = len(matriz)
k = 0
while k < n:
  print(matriz[i][j], end=" ")
  print(matriz[i][j+1], end=" ")
  print(matriz[i+1][j], end=" ")
  print(matriz[i+2][j], end=" ")
  print(matriz[i+1][j+1], end=" ")
  print(matriz[i][j+2], end=" ")
  print(matriz[i+1][j+2], end=" ")
  print(matriz[i+2][j+1], end=" ")
  print(matriz[i+2][j+2], end=" ")
  k += 3

#a = np.flipud(matriz).diagonal()
#b = np.fliplr(matriz).diagonal()
#print(a)
#print(b)

#matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

a = np.flipud(matriz).diagonal(-2)
b = np.fliplr(matriz).diagonal(1)
z = np.flipud(matriz).diagonal()
x = np.fliplr(matriz).diagonal(-1)
c = np.flipud(matriz).diagonal(2)
zz = np.fliplr(matriz).diagonal(-3)
print(a)
print(b)
print(z)
print(x)
print(c)
print(zz)
lista = []
lista.append(z[0])
print(lista)


print("-----------------------")
matriz2 = [[1, 2, 3, 14], 
          [4, 5, 6, 15], 
          [7, 8, 9, 16],
          [10, 11, 12, 13]]

m = np.flipud(matriz2).diagonal(-3)
n = np.fliplr(matriz2).diagonal(2)
print(m)
print(n)
print("-----------------------")
matriz3 = [[1,2],
           [3,4]]
m = np.flipud(matriz3).diagonal(-1)
n = np.fliplr(matriz3).diagonal(-1)
print(m)
print(n)

# Program to print matrix in Zig-zag pattern
matriz4 = [[12, 23, 3], 
          [44, 65, 62], 
          [74, 98, 95]]

def zigzag(matrix):
  rows= len(matrix)
  columns= len(matrix)

  solution=[[] for i in range(rows+columns-1)]

  for i in range(rows):
    for j in range(columns):
      sum=i+j
      if(sum%2 ==0):

        #add at beginning
        solution[sum].insert(0,matrix[i][j])
      else:

        #add at end of the list
        solution[sum].append(matrix[i][j])
      
        
  # print the solution as it as
  for i in solution:
    for j in i:
      print(j,end=" ")

zigzag(matriz4)

def recorridoDiagonalMatriz2(matriz,listaNum = [] ,diagonalNormal = (len(matriz) - 1)*(-1), diagonalInvertida = len(matriz) - 2):
                                 
  if(len(matriz) == 1):                                 
    a = np.flipud(matriz).diagonal()
    listaNum.append(a)

  if(len(matriz) == 2):                                 
    a = np.flipud(matriz).diagonal(-1)
    b = np.fliplr(matriz).diagonal()
    c = np.flipud(matriz).diagonal(1)
    listaNum.append(a), listaNum.append(b), listaNum.append(c)

  else:
    for i in range(len(matriz)):                          
      a = np.flipud(matriz).diagonal(diagonalNormal)      
      b = np.fliplr(matriz).diagonal(diagonalInvertida)   
      listaNum.append(a)                                 
      if b.size > 0:                                      
        listaNum.append(b)                               
      diagonalNormal += 2                                 
      diagonalInvertida -= 2                                                    
      fixed = [list(arr) for arr in listaNum]             
  return fixed

recorridoDiagonalMatriz2(matriz4)

def recorridoDiagonalMatrizRecursivo(matriz, diagonalNormal=0, diagonalInvertida=0, listaNum=[], c=0):                
                                          
  if(len(matriz) == 1):                                 
    a = np.flipud(matriz).diagonal()
    listaNum.append(a)

  if(len(matriz) == 2):                                 
    a = np.flipud(matriz).diagonal(-1)
    b = np.fliplr(matriz).diagonal()     
    c = np.flipud(matriz).diagonal(1)
    listaNum.append(a), listaNum.append(b), listaNum.append(c)

  else:
    if(c == len(matriz)):
      return listaNum
    else:
      if(c == 0):
        diagonalNormal = (len(matriz) - 1)*(-1)
        diagonalInvertida = len(matriz) - 2
        fixed = [list(arr) for arr in listaNum]   
      a = np.flipud(matriz).diagonal(diagonalNormal)      
      b = np.fliplr(matriz).diagonal(diagonalInvertida)    
      listaNum.append(a)                                   
      if b.size > 0:                                      
        listaNum.append(b)
                                                           

      return recorridoDiagonalMatrizRecursivo(matriz, diagonalNormal + 2, diagonalInvertida - 2, fixed, c + 1, )                                   

recorridoDiagonalMatrizRecursivo(matriz4)