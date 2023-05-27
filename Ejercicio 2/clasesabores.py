class sabores:
    __idsab = int('0')
    __nombre = ''
    __ingredientes = ''
    def __init__(self,id,nombres,ing):
        self.__idsab=id
        self.__nombre=nombres
        self.__ingredientes=ing
    def __str__(self):
        return f"ID: {self.__idsab} Nombre: {self.__nombre} Ingredientes: {self.__ingredientes}"
    