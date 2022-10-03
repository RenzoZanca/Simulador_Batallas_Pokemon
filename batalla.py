# -*- coding: utf-8 -*-

#Lukas Philippi Y.
#Renzo Zanca R.

from diccionarios import *
from movimiento import *
from pokemon import *
from entrenador import *
import random

#class Batalla:
#atributos:
#dpk: dict{str: list[any]}
#dm: dict{str:list[any]}
#ddeb: dict{str:list[str]}
#dres: dict{str:list[str]}
#dinm: dict{str:list[str]}

class Batalla:

    #Constructor
    def __init__(self,dpk=cargarPokemon("pokemon.txt"),dm=cargarMovimientos("movimientos.txt"),deb=debilidades,res=resistencias,inm=inmunidades):
       self.__pokemones=dpk
       self.__movimientos=dm
       self.__debilidades=deb
       self.__resistencias=res
       self.__inmunidades=inm
               
    #metodos auxiliares:
        
    # devPokemon: int -> Pokemon
    # Entrega un pokemon segun su id sacado de diccionario de pokemones,
    # pero sin lista de movimientos.
    def devPokemon(self,n):
        assert type(n) == int and n<151
        D=self.__pokemones
        #recorrer el diccionario de pokemons:
        for e in D:
            if int(D[e][0]) == n:
                return Pokemon(e,D[e],None)
            
    # devMovimiento: int -> Movimiento
    # Entrega un Movimiento segun su id sacado de un diccionario de movimientos
    def devMovimiento(self,n):
        assert type(n) == int and n<718
        D=self.__movimientos
        #recorrer el diccionario de movimientos:
        for e in D:
            if int(D[e][0]) == n:
                return Movimiento(e,D[e])
            
    #movTipo: Pokemon -> list[int]
    #dado un pokemon devuelve una lista con los id de todos los movimientos
    #del mismo tipo/s del pokemon
    def movTipo(self,pok):
        tipo1=pok.getTipo1()
        tipo2=pok.getTipo2()
        l=[] #lista de salida
        d=self.__movimientos
        #recorrer el diccionario de movimientos:
        for mov in d:
            if d[mov][5]==tipo1 or d[mov][5]==tipo2:
                l.append(d[mov][0])          
        return l
    
    #listaMovimientos: None -> list[int]:
    #devuelve una lista con los identificadores de todos los movimientos
    def listaMovimientos(self):
        l=[] #lista de salida
        D=self.__movimientos
        for mov in D:
            l.append(D[mov][0])
        return l
       
    #crearListaPokemon: None -> list[Pokemon]
    #Lee el diccionario de pokemon y retorna una lista con 6 pokemon distintos
    def crearListaPokemon(self):
        l=[]  #lista de salida:
        lnombres=[] #lista solo con nombres:
        i=0 #contador
        while i<6:
            n=random.randint(0,150)
            pk=self.devPokemon(n)
            nombre=pk.getNombrePk()
            #condicion para que no se repitan los pokemon:
            if nombre not in lnombres:
                lnombres.append(nombre)
                l.append(pk)
                i+=1 
        return l
 
    #asignarMovimientos: list[Pokemon] -> list[Pokemon]
    #recibe una lista de pokemon y retorna otra con movientos asignados a los pokemons
    def asignarMovimientos(self,listaInicial):
        assert type(listaInicial)==list
        listaMovimientos=self.listaMovimientos() #lista todos los id de los movs
        #iterar para cada pokemon:
        for pok in listaInicial:
            mismoTipo=self.movTipo(pok) #lista id mismo tipo
            lmov=[]   #lista de movimientos de 1 pokemon
            listaIdPk=[]   #lista con los id de los movimientos de 1 pokemon:
            
            #asignar 2 movimiento del mismo tipo:
            j=0     #contador
            while j<2:
                n1=random.randint(0,len(mismoTipo))
                #condicion para no repetir movimientos
                if n1 not in listaIdPk:
                    listaIdPk.append(n1)
                    mov=self.devMovimiento(int(mismoTipo[n1-1]))
                    lmov.append(mov)
                    pok.setAtaques(lmov)
                    j+=1
                    
            #los otros 2 movimientos los asignamos al azar:
                
            i=0 #contador
            while i<2:
                n2=random.randint(0,len(listaMovimientos))
                if n2 not in listaIdPk:
                    listaIdPk.append(n2)
                    nuevoMov=self.devMovimiento(int(listaMovimientos[n2-1]))
                    lmov.append(nuevoMov)
                    pok.setAtaques(lmov) 
                    i +=1
        return listaInicial 
       
    #crearEntrenador: str -> Entrenador
    #Recibe un nombre, luego con los 2 metodos anteriores crea una lista de
    #pokemon, para luego retornar un entrenador con el nombre y la lista
    def crearEntrenador(self,nombre):
        assert type(nombre)==str
        l1=self.crearListaPokemon()
        l2=self.asignarMovimientos(l1)
        return Entrenador(nombre,l2)
    
    # metodos aux para el ataque
    
    # factorRel: str str -> int
    # Entrega el factor que se le aplica al daño segun la relacion entre 2 tipos,
    # resistencia o debilidad.
    # por ejemplo factorRel(agua, fuego) devuelve 0.5
    def factorRel(self, tMov, tPk):
        assert type(tMov) == str and type(tPk) == str
        if tMov in self.__resistencias[tPk]:
            return 0.5
        if tMov in self.__debilidades[tPk]:
            return 2
        else:
            return 1
    
    #aplicarAtaque: Pokemon x2 Movimiento -> None
    #recibe un pokemon pk1, un movimiento y otro pokemon pk2 (pk1 aplica ataque a pk2)
    #El metodo aplica el dano producido de generar el ataque sobre pk2
    def aplicarAtaque(self,pk1,pk2,mov):
        #verificar si le achunta:
        precision=mov.getPrecision()
        n1=random.randint(1,100)
        if n1>=precision:
            print(pk1.getNombrePk()+" fallo")
            return None
        
        #inmunidad:
        tipoAtaque=mov.getTipoMov()
        pk2Tipo1=pk2.getTipo1()
        pk2Tipo2=pk2.getTipo2()
        #pokemon de 1 tipo:
        if pk2Tipo2==None:
            if tipoAtaque in self.__inmunidades[pk2Tipo1]:
                print("El ataque fallo pues "+str(pk2.getNombrePk())+" es inmune")
                return None
        #pokemon de 2 tipos:
        else:
            if tipoAtaque in self.__inmunidades[pk2Tipo1] or tipoAtaque in self.__inmunidades[pk2Tipo2]:
                print("El ataque fallo pues "+str(pk2.getNombrePk())+" es inmune")
                return None
        
        #danoBase:
        movPoder=mov.getPoder()
        pk1ATK=pk1.getAtaque()
        pk2DEF=pk2.getDefensa()
        #pre condicion para ataques especiales, donde redefinimos las variables:
        if mov.getNaturaleza() == "Especial":
            pk1ATK=pk1.getAtaqueSP()
            pk2DEF=pk2.getDefensa() 
        
        dano = (0.84 * movPoder * (pk1ATK/pk2DEF)) + 2
        
        #debilidades y resistencias:
        f1 = self.factorRel(tipoAtaque, pk2Tipo1)
        if pk2Tipo2 == None:
            dano = dano*f1
            if f1 > 1:
                print("ES MUY EFECTIVO")
            if f1 < 1:
                print("NO ES MUY EFECTIVO")
        else:
            f2 = self.factorRel(tipoAtaque, pk2Tipo2)
            dano = dano*f1*f2
            if f1 * f2 > 1:
                print("ES MUY EFECTIVO")
            if f1 * f2 < 1:
                print("NO ES MUY EFECTIVO")

        #bonus:     
   
        #stab:
        pk1Tipo1=pk1.getTipo1()
        pk1Tipo2=pk1.getTipo2()
        if tipoAtaque == pk1Tipo1 or tipoAtaque == pk1Tipo2:
            dano=dano*1.5
            
        #dano critico:
        n2=random.randint(1,10000)
        if n2 <= 625:
            dano=dano*1.5
            print("dano critico")
            
        #ponderacion final:
        n3=random.randint(85,100)
        danoFinal=int(round((dano*(n3/100)),0))
        #verificar si el danoFinal no es mayor que los ps del pk2:
        ps=pk2.getPSActuales()
        if danoFinal > ps:
            danoFinal = ps
        #cambiar PS del pokemon 2:
        pk2.setPSActuales(max(0,pk2.getPSActuales()-danoFinal))
        print(pk2.getNombrePk() + " recibe " + str(danoFinal) + " de daño dejandolo con " + str(pk2.getPSActuales()) + " PS")
        if pk2.getPSActuales() == 0: #Si pokemon es derrotado por ataque
            pk2.setEstado(False)
        return None
    
    #aplicarForcejeo: Pokemon x2 -> None
    #recibe un pokemon pk1 y otro pokemon pk2 (pk1 aplica ataque a pk2)
    #el metodo aplica el dano producido de generar el ataque sobre pk2
    #realiza el ataque forcejeo, un ataque fisico con poder 50, tipo normal,
    #precision 100, prioridad 0 y PP infinito. Luego de ejecutar dicho ataque,
    #el pokemon perdera 25 % de sus PS originales
    def aplicarForcejeo(self, pk1, pk2):
        #danoBase:
        movPoder=50
        pk1ATK=pk1.getAtaque()
        pk2DEF=pk2.getDefensa()
        dano = (0.84 * movPoder * (pk1ATK/pk2DEF)) + 2
        #stab:
        tipoAtaque="Normal"
        pk1Tipo1=pk1.getTipo1()
        pk1Tipo2=pk1.getTipo2()
        if tipoAtaque == pk1Tipo1 or tipoAtaque == pk1Tipo2:
            dano=dano*1.5
            
        #dano critico:
        n2=random.randint(1,10000)
        if n2 <= 625:
            dano=dano*1.5
            print("dano critico")   
        #ponderacion final:
        n3=random.randint(85,100)
        danoFinal=int(round((dano*(n3/100)),0))
        #verificar si el danoFinal no es mayor que los ps del pk2:
        ps=pk2.getPSActuales()
        if danoFinal > ps:
            danoFinal = ps
        pk2.setPSActuales(max(0,pk2.getPSActuales()-danoFinal))
        print(pk2.getNombrePk() + " recibe " + str(danoFinal) + " de daño dejandolo con " + str(pk2.getPSActuales()) + " PS")
        #si pokemon es derrotado por ataque:
        if pk2.getPSActuales() == 0: 
            pk2.setEstado(False)
        #perder vida por forcejeo:
        ps=pk1.getPSActuales()
        nuevops=int(ps*0.75)
        pk1.setPSActuales(nuevops)
        print(pk1.getNombrePk()+" perdio "+str(int(nuevops/3))+" de vida al aplicar forcejeo")
        return None
