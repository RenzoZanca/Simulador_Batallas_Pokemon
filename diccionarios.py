# -*- coding: utf-8 -*-

#Lukas Philippi Y.
#Renzo Zanca R.


# Diccionarios con informacion del juego

# Diccionario de debilidades de cada tipo
# Por ejemplo, pokemon tipo Fuego son debiles contra ataques tipo Roca, Tierra y Agua
debilidades = {
    "Fuego": ["Roca", "Tierra", "Agua"],
    "Roca": ["Agua", "Planta", "Acero", "Lucha", "Tierra"],
    "Tierra": ["Agua", "Planta", "Hielo"],
    "Agua": ["Electrico", "Planta"],
    "Planta": ["Bicho", "Fuego", "Veneno", "Volador", "Hielo"],
    "Acero": ["Fuego", "Tierra", "Lucha"],
    "Lucha": ["Volador", "Psiquico", "Hada"],
    "Hielo": ["Lucha", "Acero", "Roca", "Fuego"],
    "Electrico": ["Tierra"],
    "Bicho": ["Roca", "Fuego", "Volador"],
    "Veneno": ["Tierra", "Psiquico"],
    "Volador": ["Roca", "Hielo", "Electrico"],
    "Psiquico": ["Siniestro", "Fantasma"],
    "Hada": ["Acero", "Veneno"],
    "Siniestro": ["Lucha", "Bicho", "Hada"],
    "Fantasma": ["Siniestro", "Fantasma"],
    "Dragon": ["Dragon", "Hada", "Hielo"],
    "Normal": ["Lucha"],
    "": []
}

# Diccionario de resistencias de cada tipo
# Por ejemplo, pokemon tipo Bicho resisten ataques tipo Lucha, Planta y Tierra
resistencias = {
    "Acero": ["Acero", "Bicho", "Dragon", "Hada", "Hielo", "Normal", "Planta", "Psiquico", "Roca", "Volador"],
    "Agua": ["Acero", "Agua", "Fuego", "Hielo"],
    "Bicho": ["Lucha", "Planta", "Tierra"],
    "Dragon": ["Agua", "Electrico", "Fuego", "Planta"],
    "Electrico": ["Acero", "Electrico", "Volador"],
    "Fantasma": ["Bicho", "Veneno"],
    "Fuego": ["Acero", "Bicho", "Fuego", "Hada", "Hielo", "Planta"],
    "Hada": ["Bicho", "Lucha", "Siniestro"],
    "Hielo": ["Hielo"],
    "Lucha": ["Bicho", "Roca", "Siniestro"],
    "Normal": [],
    "Planta": ["Agua", "Electrico", "Planta", "Tierra"],
    "Psiquico": ["Lucha", "Psiquico"],
    "Roca": ["Fuego", "Normal", "Veneno", "Volador"],
    "Siniestro": ["Fantasma", "Siniestro"],
    "Tierra": ["Roca", "Veneno"],
    "Veneno": ["Bicho", "Hada", "Lucha", "Planta", "Veneno"],
    "Volador": ["Bicho", "Lucha", "Planta"],
    "": []
}

# Diccionario de inmunidades de cada tipo
# Por ejemplo, pokemon tipo Fantasma son inmunes contra ataques tipo Normal y Lucha
inmunidades = {
    "Acero": ["Veneno"],
    "Agua": [],
    "Bicho": [],
    "Dragon": [],
    "Electrico": [],
    "Fantasma": ["Normal", "Lucha"],
    "Fuego": [],
    "Hada": ["Dragon"],
    "Hielo": [],
    "Lucha": [],
    "Normal": ["Fantasma"],
    "Planta": [],
    "Psiquico": [],
    "Roca": [],
    "Siniestro": ["Psiquico"],
    "Tierra": ["Electrico"],
    "Veneno": [],
    "Volador": ["Tierra"],
    "": []
}


#cargarPokemon: str -> dict{str: list[any]}
#Crea un diccionario con cada pokemon y sus atributos
#a base de un archivo de texto (pokemon.txt)
def cargarPokemon(nombre):
    salida = {}
    archivo = open(nombre, "r")
    while True:
        linea = archivo.readline()
        if linea == "": break #condicion salida
        #precondicion para eliminar primera linea del archivo:
        if linea[0].isdigit():
            pokemon = linea[:-1].split(",")
            nombre = pokemon[1]
            pokemon.remove(pokemon[1])
            #si no existe el segundo tipo del pokemon:
            if pokemon[2] == "": pokemon[2] = None
            salida[nombre] = pokemon
    archivo.close()
    return salida
    


#cargarMovimientos: str -> dict{str:list[any]}
#lee un arvicho (movimientos.txt) y retorna un diccionario donde la llave de este
#corresponde al nombre de un ataque, en tanto que el valor asociado es una lista
#con los siguientes parametros (en orden): id poder (BP), PP, precision,
#prioridad, tipo y naturaleza.
def cargarMovimientos(nombre):
    archivo = open(nombre,"r")
    d={}
    #iterar para cada linea
    for linea in archivo:
        #precondicion para eliminar primera linea del archivo:
        if linea[0].isdigit():
            lista=linea.split(",")
            nombre=lista[5]
            #agregamos el id:
            ident=lista[0]
            poder=lista[1]
            pp=lista[2]
            precision=lista[3]
            prioridad=lista[4]
            tipo=lista[6]
            naturaleza=lista[7][:-1]
            #lista del diccionario:
            nuevaLista=[ident,poder,pp,precision,prioridad,tipo,naturaleza]
            #definir elemento del diccionario:
            d[nombre]=nuevaLista
    archivo.close()
    return d
        

    
