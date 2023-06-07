from claseempleado import empleados

class contratado(empleados):
    __fechainicio=''
    __fechafin=''
    __cantidadhoras=int('0')
    __valorhora=float('0')
    def __init__(self,dni,nombre,direccion,telefono,fechainicio,fechafin,cantidadhoras,valorhora):
        super().__init__(dni,nombre,direccion,telefono)
        self.__fechainicio=fechainicio
        self.__fechafin=fechafin
        self.__cantidadhoras=cantidadhoras
        self.__valorhora=valorhora
    def __str__(self):
        return f"DNI: {self.__dni} Nombre: {self.__nombre} Direccion: {self.__direccion} Telefono: {self.__telefono} Fecha Inicio: {self.__fechainicio} Fecha Fin: {self.__fechafin} Cantidad horas: {self.__cantidadhoras} Valor por hora: {self.__valorhora}"
    def mostrarhoras(self):
        return self.__cantidadhoras
    def aumentarhoras(self,horas):
        self.__cantidadhoras+=horas
        return
    def calcularsueldo(self):
        sueldo=self.__cantidadhoras*self.__valorhora