from claseempleado import empleados
class externo(empleados):
    __tarea=''
    __fechainicio=''
    __fechafin=''
    __montoviatico=float('0')
    __costoobra=float('0')
    __montosegurovida=float('0')
    def __init__(self,dni,nombre,direccion,telefono,tarea,fechainicio,fechafin,montoviatico,costoobra,montosegurovida):
        super().__init__(dni,nombre,direccion,telefono)
        self.__tarea=tarea
        self.__fechainicio=fechainicio
        self.__fechafin=fechafin
        self.__montoviatico=montoviatico
        self.__costoobra=costoobra
        self.__montosegurovida=montosegurovida
    def __str__(self):
        return f"DNI: {self.__dni} Nombre: {self.__nombre} Direccion: {self.__direccion} Telefono: {self.__telefono} Fecha Inicio: {self.__fechainicio} Fecha Fin: {self.__fechafin} Monto viatico: {self.__montoviatico} Costo obra: {self.__costoobra} Monto seguro de vida: {self.__montosegurovida}"
    def calcularsueldo(self):
        sueldo=self.__costoobra-self.__montoviatico-self.__montosegurovida
        return sueldo