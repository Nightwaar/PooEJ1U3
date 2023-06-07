import numpy as np
import csv
from clasecontratado import contratado
from claseexterno import externo
from claseplanta import planta
from claseempleado import empleados
class manejador(object):
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension=10, incremento=5):
        self.__empleados = np.empty(dimension, dtype=empleados)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento=incremento
    def agregarInscripcion(self, unEmpleado):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__empleados.resize(self.__dimension)
        self.__empleados[self.__cantidad]=unEmpleado
        self.__cantidad += 1
    def cargar(self):
        archivo=open('planta.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            self.agregarInscripcion(planta(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]))
        archivo=open("contratados.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            self.agregarInscripcion(contratado(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6]))
        archivo=open("externos.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            self.agregarInscripcion(externo(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9]))
    def accion1(self,dni,horas):
        bandera=False
        i=0
        while bandera!=True and i<len(self.__empleados):
            if self.__empleados.dni()==dni:
                self.__empleados.aumentarhoras(horas)
    def accion3(self):
        for empleado in range(len(self.__empleados)):
            sueldo=int(self.__empleados[empleado].calcularsueldo())
            if sueldo<150000:
                self.__empleados[empleado].mostrarempleado()
    def accion4(self):
        for empleado in range(len(self.__empleados)):
            print(self.__empleados[empleado].nombre())
            print(self.__empleados[empleado].telefono())
            print(self.__empleados[empleado].calcularsueldo())