def potencia(numero, potencia1, nuevo_numero):
  if potencia1 == 1:
    return nuevo_numero
  else: 
    resultado = nuevo_numero * numero
  return potencia(numero, potencia1-1, resultado)
  
potencia(2, 8, 2)
