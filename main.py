# -*- coding: utf-8 -*-

#Lukas Philippi Y.
#Renzo Zanca R.

from batalla import *
import random

#class Main
#atributos:
#b: Batalla

class Main:
    
    #constructor:
    def __init__(self,b=Batalla()):
        self.__b = b
        self.__usuario=b.crearEntrenador("") #entrenador
        self.__rival=b.crearEntrenador("") #entrenador
        self.__listaUsuario = self.__usuario.getListaPokemon() #listaPk
        self.__listaRival = self.__rival.getListaPokemon() #listaPk
        self.__pkActualUsuario = self.__usuario.getpokeActual() #pk actual
        self.__pkActualRival = self.__rival.getpokeActual() #pk actual
        self.__pkActivosUsuario=6
        self.__pkActivosRival=6
        
    #getPkActivosUsuario: None -> int
    #devuelve la cantidad de pokemons activos del usuario
    def getPkActivosUsuario(self):
        return self.__pkActivosUsuario

    #getPkActivosRival: None -> int
    #devuelve la cantidad de pokemons activos del rival
    def getPkActivosRival(self):
        return self.__pkActivosRival       
    
    #setPkActivosUsuario: int -> None
    #modifica la cantidad de pokemons activos del usuario
    def setPkActivosUsuario(self,n):
        assert type(n) == int
        self.__pkActivosUsuario=n
 
    #setPkActivosRival: int -> None
    #modifica la cantidad de pokemons activos del rival
    def setPkActivosRival(self,n):
        assert type(n) == int
        self.__pkActivosRival=n
    
    
    #metodos auxiliares:
        
    #mostrarEquipo: list[Pokemon] -> None
    #muestra en pantalla los pokemons del usuario y sus respectivos movimientos
    def mostrarEquipo(self,lista):
        assert type(lista)==list
        i=1 #contador
        #iterar para cada pokemon:
        for pk in lista:
            print(str(i)+"."+str(pk))
            movs=pk.getAtaques()
            print("Movimientos: "+str(movs[0].getNombreMov())+", "+str(movs[1].getNombreMov())+", "+str(movs[2].getNombreMov())+", "+str(movs[3].getNombreMov()))
            print("")
            i+=1
        return
    
    #intro: None -> None
    #da una introduccion al simulador de batallas pokemon
    #pide los nombres de los 2 entrenadores y muestra el equipo del usuario
    def intro(self):
        print("")
        print("Bienvenido al simulador de batallas Pokemon!")
        #nombre entrenadores:
        nombreUsuario=str(input("¿Cual es tu nombre, entrenador/a? "))
        self.__usuario.setNombreEntrenador(nombreUsuario)
        print("Hola "+nombreUsuario)
        nombreRival=str(input("¿Cual es el nombre de tu rival? "))
        self.__rival.setNombreEntrenador(nombreRival)
        print("")
        #mostrar equipo usuario:
        print("Este es tu equipo:")
        print("")
        self.mostrarEquipo(self.__listaUsuario)
        print("")
        print("Muy bien, a iniciar la batalla!")
        print("")
        return None
        
    #mostrarPkActivos: None -> None
    #muestra los pokemons activos del usuario y el rival
    def mostrarPkactivos(self):
        print("Pokemon de "+ self.__usuario.getNombreEntrenador() +":")
        print(str(self.__pkActualUsuario))
        print("Pokemon de "+ self.__rival.getNombreEntrenador() +":")
        print(str(self.__pkActualRival))
        return None
    
    #atacar: None -> list[Movimiento, int, int]
    # Eliges un movimiento de la lista de tu pokemon, y entrega una lista de datos 
    # que se usaran para el ataque.
    # si no quedan PP de ningun ataque, se aplica forecejeo.
    def atacar(self):
        pk=self.__pkActualUsuario
        #condicion donde ya no le quedan PP al pokemon y se aplica forcejeo:
        i=0 #contador
        #iterar para cada movimiento:
        for mov in pk.getAtaques():
            n=mov.getPP_actuales()
            i+=n
        if i==0:
            Velocidad = pk.getVelocidad()
            #definimos el movimiento forcejeo como None
            return [None, 0, Velocidad]
        print("")
        print("Ataques de " + pk.getNombrePk() + ":")
        j = 1 #contador
        #mostrar movimientos:
        for e in pk.getAtaques():
            print("(" + str(j) + ")  " + str(e))
            j += 1
        print("")
        e1 = int(input("Elige uno de estos ataques poniendo su debido numero "))
        if e1==1 or e1==2 or e1==3 or e1==4:
            mov=pk.getAtaques()[e1-1]
            #condicion ataque sin PP:
            if mov.getPP_actuales()==0:
                print("No lo quedan PP a ese ataque")
                return self.atacar()
            #modificar los PP:
            PPactuales=mov.getPP_actuales()
            mov.setPP_actuales(PPactuales-1)
            #definimos y retornamos datos que seran relevantes a la hora de atacar: 
            Prioridad = mov.getPrioridad()
            Velocidad = pk.getVelocidad()
            return [mov, Prioridad, Velocidad]
                
        else: #numero mal ingresado
            print("Escoge un numero del 1 al 4")
            return self.atacar()
        
    #cambiarPkUsuario: None -> None
    #cambia el pokemon del usuario
    def cambiarPkUsuario(self):
        print("")
        self.mostrarEquipo(self.__listaUsuario)
        while True:
           n=int(float(input("Escoge el numero del pokemon al que quieres cambiar ")))
           if n > 0 and n < 7:
               print("")
               pk=self.__listaUsuario[n-1]
               estado=pk.getEstado()
               #verificar que no este derrotado de antes:
               if estado==False:      
                   print("Este pokemon fue derrotado, escoge uno activo")
               #verificar que no escoja el mismo que esta en combate:
               elif pk == self.__pkActualUsuario:
                   print(pk.getNombrePk() + " ya esta en combate, debes elegir otro")
               else: 
                   self.__pkActualUsuario = pk
                   print(pk.getNombrePk()+" yo te elijo!")
                   print("")
                   break
           else: #numero mal ingresado
               print("")
               print("Numero invalido")

        
    #accion: None -> list[Movimiento, int, int]
    #pregunta un numero al usuario
    #ejecuta un ataque si se ingresa 1
    #ejecuta un cambio de pokemon si se ingresa 2
    def accion(self):
        print("")
        print("Que quieres hacer en tu turno?")
        n=int(input("Atacar (1) - Cambiar Pokemon Activo (2)? "))
        if n==1:
            a = self.atacar()
            return a
        elif n==2:
            #precondicion para no cambiar si solo queda 1 pokemon
            if self.__pkActivosUsuario == 1:
                print("Este es tu ultimo pokemon!! no puedes cambiarlo !!")
                return self.accion()
            self.cambiarPkUsuario()
            return []
        else:
            print("Tienes que escribir '1' o '2'")
            return self.accion()
        
    
    #turnoRival: None -> [Movimiento, int, int]
    # Rival elige un ataque al azar y lo prepara.
    # Aqui tambien se ve el caso de forcejeo
    def turnoRival(self):
        pk = self.__pkActualRival
        #Ahora rival ataca
        #condicion donde ya no le quedan PP al pokemon y aplica forcejeo:
        i=0 #contador
        for mov in pk.getAtaques():
            n=mov.getPP_actuales()
            i+=n
        if i==0:
            Velocidad = pk.getVelocidad()
            #definimos el movimiento forcejeo como None
            return[None, 0, Velocidad]
        
        #si no hay forcejeo:
        m = random.randint(0, 3)
        mov=pk.getAtaques()[m]
        if mov.getPP_actuales==0:
                return self.turnoRival()
            #modificar los PP:
        PPactuales=mov.getPP_actuales()
        mov.setPP_actuales(PPactuales-1)
        Prioridad = mov.getPrioridad()
        Velocidad = pk.getVelocidad()
        return [mov, Prioridad, Velocidad]
    
    # pkUsuarioDerrotado: None -> None
    # revisa si el pokemon actual del usuario esta derrotado, si es asi
    # pide reemplazarlo por otro
    def pkUsuarioDerrotado(self):
        #verificar si esta derrotado:
        if self.__pkActualUsuario.getPSActuales() == 0:
            #Condición ultimo pk derrotado:
            if self.__pkActivosUsuario == 1: 
                print(self.__pkActualUsuario.getNombrePk() + " a sido derrotado ! ! !")
                self.setPkActivosUsuario(0)
                return
            actUsuario=self.getPkActivosUsuario()
            self.setPkActivosUsuario(actUsuario -1)
            print("")
            print(self.__pkActualUsuario.getNombrePk() + " a sido derrotado ! ! !")
            print("Te quedan "+str(self.getPkActivosUsuario())+" pokemon")
            print("")
            print("Debes elegir un nuevo pokemon")
            self.cambiarPkUsuario()
        return
    
    # pkRivalDerrotado: None -> None
    # Revisa si el pokemon actual del rival fue derrotado, si este es el caso,
    # lo cambia por el siguente de la lista
    def pkRivalDerrotado(self):
        pk = self.__pkActualRival
        PSfinal = pk.getPSActuales()
        # precondicion si el pokemon actual del rival fue derrotado
        if PSfinal == 0:
            #precondicion por si cae el ultimo pokemon Rival
            if self.__pkActivosRival ==1:
                print(pk.getNombrePk()+" fue derrotado ! ! !")
                self.setPkActivosRival(0)
                return
            print(pk.getNombrePk()+" fue derrotado ! ! !")
            actRival=self.getPkActivosRival()
            self.setPkActivosRival(actRival-1)
            print("A "+self.__rival.getNombreEntrenador()+" le quedan "+str(self.getPkActivosRival())+" pokemon")
            #cambiar pokemon rival:
            x=self.__pkActualRival
            n=self.__listaRival.index(x)
            print("")
            self.__pkActualRival = pk=self.__listaRival[n+1]
            print(self.__rival.getNombreEntrenador() + " elige a " + self.__pkActualRival.getNombrePk() + "! ! !")
            print("")
        return
        
    #ataqueUsuario: Movimiento -> None
    #recibe un movimiento para luego ejecutarlo
    #primero verifica que el pokemon del rival este activo
    #luego verifica si se debe aplicar forcejeo o no
    def ataqueUsuario(self,mov):
        #pokemones
        pkUsuario = self.__pkActualUsuario
        pkRival = self.__pkActualRival
        #condicion rival inactivo
        if pkUsuario.getEstado() == False:
            return
        #condicion forcejeo:
        elif mov == None:
            print("")
            print(self.__pkActualUsuario.getNombrePk()+" uso forcejeo")
            self.__b.aplicarForcejeo(self,pkUsuario,pkRival)
            return
        else:
            print("")
            print(self.__pkActualUsuario.getNombrePk()+" uso "+mov.getNombreMov())
            self.__b.aplicarAtaque(pkUsuario, pkRival, mov)
            return
        
    #ataqueRival: Movimiento -> None
    #recibe un movimiento para luego ejecutarlo
    #primero verifica que el pokemon del usuario este activo
    #luego verifica si se debe aplicar forcejeo o no
    def ataqueRival(self,mov):
        #pokemones
        pkUsuario = self.__pkActualUsuario
        pkRival = self.__pkActualRival
        #condicion usuario inactivo
        if pkRival.getEstado() == False:
            return
        #condicion forcejeo:
        elif mov == None:
            print("")
            print(self.__pkActualRival.getNombrePk()+" uso forcejeo")
            self.__b.aplicarForcejeo(self,pkRival,pkUsuario)
            return
        else:
            print("")
            print(self.__pkActualRival.getNombrePk()+" uso "+mov.getNombreMov())
            self.__b.aplicarAtaque(pkRival,pkUsuario,mov)        
            return
    
    
    # ataquesRonda: list[Movimiento, Int, Int] -> None
    # Revisa prioridades y velocidades de ataques para ver que ataque va primero
    # y luego los aplica
    def ataquesRonda(self,listaUsuario, listaRival):
        assert type(listaUsuario) == list and type(listaRival) == list
        #pokemones
        pkUsuario = self.__pkActualUsuario
        pkRival = self.__pkActualRival
        
        #condicion si el usuario escogio cambiar de pokemon
        if listaUsuario==[]:
            self.ataqueRival(listaRival[0])
            return None

        if listaUsuario[1] > listaRival[1]: #Tu tienes mas prioridad
            self.ataqueUsuario(listaUsuario[0])
            self.ataqueRival(listaRival[0])
            
        elif listaUsuario[1] < listaRival[1]: # Rival tienes mas prioridad
            self.ataqueRival(listaRival[0])
            self.ataqueUsuario(listaUsuario[0])
            
        else: # Tienen misma prioridad
        
            if listaUsuario[2] > listaRival[2]: #Tu pk tienes mas velocidad
               self.ataqueUsuario(listaUsuario[0])
               self.ataqueRival(listaRival[0])
                
            elif listaUsuario[2] < listaRival[2]: #El pk rival tienes mas velocidad
                self.ataqueRival(listaRival[0])
                self.ataqueUsuario(listaUsuario[0])
                
            else: #Si tienen velocidad Y prioridades iguales ataca el usuario primero
                self.ataqueUsuario(listaUsuario[0])
                self.ataqueRival(listaRival[0])
            

    # Programa que simula batalla pokemon, no necesita receta
    def run(self):
        self.intro()
        while True:
            #verificar que los pokemon no esten derrotados antes de empezar la ronda
            self.pkRivalDerrotado()
            self.pkUsuarioDerrotado()
            #aqui vemos el excepcional caso en que los ultimos 2 pokemon sean
            #derrotados al mismo tiempo, debido a que uno aplico forcejeo y
            #fue derrotado por los ps que pierde
            #en este caso se declara empate:
            if self.__pkActivosRival == 0 and self.__pkActivosUsuario == 0:
                print("Ambos entrenadores se han quedado sin pokemons")
                print("Se ha declarado un empate!")
                break
            #condicion gana el usuario:
            elif self.__pkActivosRival == 0:
                print("")
                print("A " + self.__rival.getNombreEntrenador() + " no le quedan Pokemon que puedan pelear! Has ganado!")
                break
            #condicion gana el rival:
            elif self.__pkActivosUsuario == 0:
                print("")
                print("Te haz quedado sin pokemon para luchar :(")
                print(self.__rival.getNombreEntrenador()+" a ganado esta vez")
                break
            else:
                print("----------------------------------------------------------------------------------------")
            print("")
            #mostrar los pokemon
            self.mostrarPkactivos()
            #preparar ataques:
            a = self.accion()
            r = self.turnoRival()
            #ejecutar ataques:
            self.ataquesRonda(a,r)
            print("")
            
        
# Aqui llamamos al programa principal (no tocar esta parte)
if __name__ == '__main__':
    Main().run()
