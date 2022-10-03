# -*- coding: utf-8 -*-

#Lukas Philippi Y.
#Renzo Zanca R.


#class Entrenador:
#atributos:
#nombre: str
#listaPokemon: list[Pokemon]

class Entrenador:

    # Constructor
    def __init__(self,nombre,listaPokemon):
        self.__nombre=nombre
        self.__listaPokemon=listaPokemon
        self.__pokeActual = listaPokemon[0] #Pokemon en combate actualmente, atributo agregado por nosotros.
    #getters y setters:
        
    #getNombreEntrenador: None -> str
    #devuelve el nombre del entrenador
    def getNombreEntrenador(self):
        return self.__nombre
    
    #setNombreEntrenador: str -> None
    #cambia el nombre del entrenador
    def setNombreEntrenador(self,nuevoNombre):
        self.__nombre = nuevoNombre
    
    #getlistaPokemon: None -> list[Pokemon]
    #devuelve la lista de pokemon del entrenador
    def getListaPokemon(self):
        return self.__listaPokemon
    
    #getpokeActua:l None-> Pokemon
    #devuelve el pokeActual
    def getpokeActual(self):
        return self.__pokeActual
          
    # setpokeActual: int -> None
    # cambia el pokemon actual a otro de la lista
    def setpokeActual(self, n):
        assert type(n) == int and n <= len(self.__listaPokemon) -1 and n >= 0
        self.__pokeActual = self.__listaPokemon[n]






