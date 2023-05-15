class carrera:
    __codigo= int('0')
    __nombre= ''
    __titulo=''
    __duracion=''
    __tipo=''
    def __init__(self,codigo,nombre,titulo,duracion,tipo):
            __codigo= codigo
            __nombre= nombre
            __titulo= titulo
            __duracion=duracion
            __tipo=tipo 
    def __str__(self):
        return f"{self.__codigo} {self.__nombre} {self.__titulo} {self.__duracion} {self.__tipo}"
    def verif(self):
        return self.__nombre
    def codigo(self):
        return self.__codigo
    def nombre(self):
        return self.__nombre