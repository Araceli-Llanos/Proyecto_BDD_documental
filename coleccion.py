import os
os.system("cls")

from documento import Document 
from str import Str2Dic

class Coleccion(object):
    def __init__ (self, nombre):
        self.nombre=nombre
        self.documentos={}
    def aniadir_documento(self,documento):
        self.documentos[documento.id] = documento
    def eliminar_documento(self,id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]
    def buscar_documentos(self,id_documento):
        return self.documentos.get(id_documento,None)
    def __str__(self):
        return f"coleccion {self.nombre} con {len(self.documentos)} documentos"
    def importar_coleccion(self,direccion):
        with open(direccion, 'rt') as file: 
            schema = file.readline().replace("\n", "")
            parser = Str2Dic(schema)
            i= 0
            line= file.readline()
            
            while line != "":
                d=Document(i,parser.converter(line))
                self.aniadir_documento(d)
                i = i+1
                line= file.readline()
    def listar(self, a):
        b = 0
        while a.buscar_documentos(b) != None:
            print(a.buscar_documentos(b))
            b=b+1


