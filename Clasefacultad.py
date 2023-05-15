from PooEJ1U3.Clasecarrera import carrera
class facultad:
    __codigo = int('0')
    __nombre= ''
    __direccion= ''
    __localidad = ''
    __telefono = int('0')
    def __init__(self,cod,nombre,dire,loc,tel):
        self.__codigo=cod
        self.__nombre=nombre
        self.__direccion=dire
        self.__localidad=loc
        self.__telefono=tel
        self.__lista= []
    def __str__(self):
        return f"{self.__codigo} {self.__nombre} {self.__direccion} {self.__localidad} {self.__telefono}"
    def app(self,codigo,nombre,titulo,duracion,tipo):
        self.__lista.append(facultad(codigo,nombre,titulo,duracion,tipo))
    def mostrarcarrera(self):
        for i in self.__lista:
            print(i)
    def codigo(self):
        return self.__codigo
    def nombre(self):
        return self.__nombre
    def localidad(self):
        return self.__localidad
    def verif(self):
        return self.__nombre
    def buscar(self,nombre):
        i=0
        bandera=False
        while bandera!=True and i< len(self.__lista):
            if self.__lista[i].verif()==nombre:
                print("El codigo de carrera es: {}".format(self.__lista[i].codigo()))
                print("El nombre es: {}".format(self.__lista[i].nombre()))
                print("La localidad es: {}".format(self.__localidad))
                bandera=True
            else:
                i+=1