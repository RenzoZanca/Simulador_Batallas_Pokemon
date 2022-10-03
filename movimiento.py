# -*- coding: utf-8 -*-

#Lukas Philippi Y.
#Renzo Zanca R.

#class Movimiento:
#atributos:
#nombre: str
#lista: list[any]

class Movimiento:

    # Constructor
    def __init__(self,nombre,lista):
        self.__nombre=nombre 
        self.__lista=lista 
        #definir los campos:
        tipo=lista[5] 
        naturaleza=lista[6] 
        poder=int(lista[1]) 
        PP=int(lista[2]) 
        precision=int(lista[3]) 
        prioridad=int(lista[4]) 
        self.__tipo=tipo 
        self.__naturaleza=naturaleza 
        self.__poder=poder 
        self.__PP=int(PP)
        self.__precision=precision 
        self.__prioridad=prioridad 
        #definimos los pp actuales, que partiran con los pp de la lista
        #luego con los metodos se modificara este valor:
        PP_actuales=PP
        self.__PP_actuales=PP_actuales
        #por ultimo, agregamos por conveniencia el campo ID:
        ID=lista[0]
        self.__ID=ID
        
    #getters y setters:
        
    #getNombreMov: None -> str
    #devuelve el nombre del movimiento
    def getNombreMov(self):
        return self.__nombre

    #getTipoMov: None -> str
    #devuelve el tipo del movimiento
    def getTipoMov(self):
        return self.__tipo
    
    #getNaturaleza: None -> str
    #devuelve la naturaleza del movimiento
    def getNaturaleza(self):
        return self.__naturaleza
    
    #getPoder: None -> int
    #devuelve el poder del movimiento
    def getPoder(self):
        return self.__poder
    
    #getPP: None -> int
    #devuelve los PP del movimiento
    def getPP(self):
        return self.__PP
    
    #getPrecision: None -> int
    #devuelve la precision del movimiento
    def getPrecision(self):
        return self.__precision
    
    #getPrioridad: None -> int
    #devuelve la prioridad del movimiento
    def getPrioridad(self):
        return self.__prioridad
    
    #getID: None -> int
    #devuelve el id del movimiento
    def getID(self):
        return self.__ID
    
    #getPP_actuales: None -> int
    #devuelve los PP actuales del movimiento
    def getPP_actuales(self):
        return self.__PP_actuales
    
    #setPP_actuales: int -> None
    #modifica los PP actuales del movimiento
    def setPP_actuales(self,x):
        assert type(x)==int
        self.__PP_actuales=x

    # Sobreescribir metodo __str__
    #__str__: None -> str
    #muestra informacion relevante para el jugador sobre el movimiento
    #ej: Hidropulso  Tipo: Agua  PP: 20/20
    def __str__(self):
        frase=self.__nombre+"  Tipo: "+self.__tipo+"  PP: "+str(self.__PP_actuales)
        return frase


