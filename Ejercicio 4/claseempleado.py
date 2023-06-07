class empleados:
    __dni=''
    __nombre=''
    __direccion=''
    __telefono=''
    def __init__(self,dni,nombre,direccion,telefono):
        self.__dni=dni
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono
    def __str__(self):
        return f"DNI: {self.__dni} Nombre: {self.__nombre} Direccion: {self.__direccion} Telefono: {self.__telefono}"
    def dni(self):
        return self.__dni
    def mostrarempleado(self):
                return f"""
DNI: {self.__dni}
Nombre: {self.__nombre}
Direccion: {self.__direccion}"""
    def nombre(self):
        return self.__nombre
    def telefono(self):
        return self.__telefono