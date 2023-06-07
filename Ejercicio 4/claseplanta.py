from claseempleado import empleados
class planta(empleados):
    __sueldo=float('0')
    __antiguedad=''
    def __init__(self,dni,nombre,direccion,telefono,sueldo,antiguedad):
        super().__init__(dni,nombre,direccion,telefono)
        self.__sueldo=float(sueldo)
        self.__antiguedad=antiguedad
    def __str__(self):
        return f"DNI: {self.__dni} Nombre: {self.__nombre} Direccion: {self.__direccion} Telefono: {self.__telefono} Sueldo: {self.__sueldo} Antiguedad: {self.__antiguedad} años"
    def calcularsueldo(self):
        porcentaje=self.__sueldo*(1/100)
        sueldo=self.__sueldo+porcentaje*self.__antiguedad
        return sueldo