# -*- coding: utf-8 -*-

#Lukas Philippi Y.
#Renzo Zanca R.

# Atributos:
# nombre: str
# listaAtr: list[any]
# listaMov: list[Movimiento]

class Pokemon:

    # Constructor
    def __init__(self, nombre, listaAtr, listaMov):
        self.__nombre = nombre
        self.__id = int(listaAtr[0]) # No pedido, pero hace la vida mas facil
        self.__tipo1 = listaAtr[1] 
        self.__tipo2 = listaAtr[2] 
        self.__PS = int(listaAtr[3])
        self.__ataque = int(listaAtr[4])
        self.__defensa = int(listaAtr[5])
        self.__ataqueSP = int(listaAtr[6])
        self.__defensaSP = int(listaAtr[7])
        self.__velocidad = int(listaAtr[8])
        self.__ataques = listaMov
        self.__PSActuales = int(listaAtr[3]) 
        self.__estado = True # Parte en "Activo" por omision (Get/Set)
        
    #Getters:
    
    # getNombre: None -> str 
    # entrega nombre el del pokemon
    def getNombrePk(self):
        return self.__nombre
    
    # getId: None -> int 
    # entrega la id del pokemon
    def getId(self):
        return self.__id
    
    # getTipo1: None -> str 
    # entrega el tipo1 del pokemon
    def getTipo1(self):
        return self.__tipo1
    
    # getTipo2: None -> str (o None)
    # entrega el tipo2 del pokemon
    def getTipo2(self):
        return self.__tipo2
    
    # getPS: None -> int 
    # entrega el PS del pokemon
    def getPS(self):
        return self.__PS
    
    # getAtaque: None -> int
    # entrega el ataque del pokemon
    def getAtaque(self):
        return self.__ataque
    
    # getDefensa: None -> int
    # entrega la defensa del pokemon
    def getDefensa(self):
        return self.__defensa
    
    # getAtaqueSP: None -> int
    # entrega el ataqueSP del pokemon
    def getAtaqueSP(self):
        return self.__ataqueSP
    
    # getDefensaSP: None -> int
    # entrega la defensaSP del pokemon
    def getDefensaSP(self):
        return self.__defensaSP
    
    # getVelocidad: None -> int
    # entrega la velocidad del pokemon
    def getVelocidad(self):
        return self.__velocidad
    
    # getAtaques: None -> list[Movimientos]
    # entrega la lista de movimientos del pokemon
    def getAtaques(self):
        return self.__ataques
    
    # getPSActuales: None -> int
    # entrega PSActuales de pokemon
    def getPSActuales(self):
        return self.__PSActuales
    
    # getEstado: None -> bool
    # entrega el estado del pokemon
    def getEstado(self):
        return self.__estado
    
    # Setters:
    
    # setPSActuales: int -> None
    # modifica el valor de self.__PSActuales
    def setPSActuales(self, n):
        assert type(n) == int
        self.__PSActuales = n
        
    # setEstado: bool -> None
    # modifica el valor de self.__estado
    def setEstado(self, n):
        assert type(n) == bool
        self.__estado = n
        
    # setAtaques: list[Movimientos] -> None
    # modifica el valor de self.__ataques
    def setAtaques(self, n):
        self.__ataques = n    
    
    # __str__: None -> str
    #muestra informacion relevante para el jugador sobre el pokemon
    #ej: Pikachu HP: 121/121 Tipo: Electrico | Estado: Activo
    def __str__(self):
        n = ""
        if self.__tipo2 != None:
            n = "," + self.__tipo2
        if self.__estado == True:
            m = "Activo"
        else:
            m = "Derrotado"
        return "  " + self.__nombre + "   HP: " + str(self.__PSActuales) + "/" + str(self.__PS) + "   Tipo: " + self.__tipo1 + n + "  | Estado: " + m 


