from coleccion import *
from documento import *

class BaseDeDatos(object):
    def __init__(self):
        self.colecciones = {}
    def crear_coleccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion]=Coleccion(nombre_coleccion)
    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones: 
            del self.colecciones[nombre_coleccion]
    def obtener_coleccion(self, nombre_coleccion):
         return self.colecciones.get(nombre_coleccion,None)
    def __str__(self):
        return f"Base de datos Documental con {len(self.coleccioness)} colecciones"
        


        


