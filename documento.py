class Document(object): 
    autoin= 0 
    def __init__(self, id, contenido=None):
         self.id = id 
         self.contenido= contenido if contenido is not None else {}
    def obtener_valor(self,clave):
        return self.contenido.get(clave, None)
    def modificar_valor(self,clave,valor):
        self.contenido[clave] = valor
    def __str__(self):
        return f"documento (id={self.id}, contenido={self.contenido})"

        





   


         




          



