def menor_lista(lista):
  if len(lista) == 1:
    return lista
  elif lista[0] > lista[-1]:
      return menor_lista(lista[1:]) 
  else:
    lista[0] < lista[-1]
    return menor_lista(lista[:-1])
menor_lista([6,2,3,4,5])
