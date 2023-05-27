import csv
from clasesabores import sabores
class mansab:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def cargar(self):
        archivo = open("sabor.csv")
        reader= csv.reader(archivo,delimiter=',')
        for fila in reader:
            self.__lista.append(sabores(fila[0],fila[1],fila[2]))
    def mostrar(self):
        for i in self.__lista:
            print (i)