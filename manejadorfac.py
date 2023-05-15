import csv
from Clasefacultad import facultad
from PooEJ1U3.Clasecarrera import carrera
class manejador:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def cargar(self):
        archivo = open('facu.csv')
        reader = csv.reader(archivo,delimiter=',')
        i=0
        for fila in reader:
            if int(fila[0])!=i:
                self.__lista.append(facultad(fila[0],fila[1],fila[2],fila[3],fila[4]))
                i+=1
            else:
                self.__lista[i-1].app(fila[1],fila[2],fila[3],fila[4],fila[5])
    def opcion1(self,i):
        i-=1
        self.__lista[i].mostrarcarrera()
    def opcion2(self,nombre):
        for carrera in self.__lista:
            carrera.buscar(nombre)

                