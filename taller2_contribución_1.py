#hay que empezar a jugar con estas pregunta para los condicionales
primera_pregunta = str(input("¿Importa el orden?: "))
segunda_pregunta = str(input("¿Intervienen todos los elementos?: "))
tercera_pregunta = str(input("¿Se repiten los elementos?: "))

class Combinaciones_Permutaciones:
  def __init__(self,numero_de_elementos,elementos_a_agrupar):
    self.m = numero_de_elementos  
    self.n = elementos_a_agrupar # cuando llamemos la clase ahi vamos a poner los datos

  def combinaciones_ordinarias(self):
    m = self.m
    n = self.n
    resta_de_la_operacion = m-n #se tiene que hacer este tipo de operaciones por parte para que no lanze un error 
    m = factorial_de_un_numero(m) 
    n = factorial_de_un_numero(n)
    resultado_resta = factorial_de_un_numero(resta_de_la_operacion) #el resultado de mi resta lo factorizo
    operacion = m//n*resultado_resta #aca ya hago toda la operecion para ordinarias
    return operacion
  
  def combinaciones_con_repeticion(self):
    m = self.m
    n = self.n
    suma_de_la_operacion = m+n-1
    resta_de_la_operacion = m-1
    m = factorial_de_un_numero(m)
    n = factorial_de_un_numero(n)
    resultado_suma = factorial_de_un_numero(suma_de_la_operacion)
    resultado_resta = factorial_de_un_numero(resta_de_la_operacion)
    operacion = resultado_suma//n*resultado_resta
    return operacion

#me surgio una idea el condicional de las preguntas va ejecutar todas mis funciones anteriores 
  def permutacion_variciones_ordinarias(self):
    m = self.m
    n = self.n
    resta_de_la_operacion = m-n
    m = factorial_de_un_numero(m)
    n = factorial_de_un_numero(n)
    resultado_resta = factorial_de_un_numero(resta_de_la_operacion)
    operacion = m//resultado_resta
    return operacion

  def permutacion_variciones_con_repeticion(self):
    m = self.m
    n = self.n
    operacion = m**n
    return operacion
  
  def permutaciones_ordinarias(self):
    m = factorial_de_un_numero(self.m)
    return m
  
  #def permutaciones_con_repeticion(self): este es el que falta crear 

  
  def devolver_valor_de_operacion(self):
    if(primera_pregunta == "si" and segunda_pregunta == "no" and tercera_pregunta == "no"):
      return self.permutacion_variciones_ordinarias()

    elif(primera_pregunta == "si" and segunda_pregunta == "no" and tercera_pregunta == "si"):
      return self.permutacion_variciones_con_repeticion()
    
    elif(primera_pregunta == "si" and segunda_pregunta == "si" and tercera_pregunta == "no"):
      return self.permutaciones_ordinarias()
    
    elif(primera_pregunta == "si" and segunda_pregunta == "si" and tercera_pregunta == "si"):
      return self.permutaciones_con_repeticion()

    #--------------------------------arriba estan las permutaciones------------------------

    elif(primera_pregunta == "no" and segunda_pregunta == "no" and tercera_pregunta == "no"):
      return self.combinaciones_ordinarias()

    else:
      if(primera_pregunta == "no" and segunda_pregunta == "no" and tercera_pregunta == "si"):
        return self.combinaciones_con_repeticion()  



p = Combinaciones_Permutaciones(6,3)
p.devolver_valor_de_operacion()
