def factorial_de_un_numero(numero):
  numero_inicial = numero
  while numero > 1:
    numero -= 1
    numero_inicial *= numero
  return numero_inicial
