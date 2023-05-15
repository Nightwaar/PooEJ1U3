import csv
from PooEJ1U3.Clasecarrera import carrera
from Clasefacultad import facultad
from manejadorfac import manejador
if __name__=='__main__':
    lista=manejador()
    lista.cargar()
    print("1.Ingrese codigo de facultad para mostrar carreras")
    print("2.Ingrese nombre de carrera para indicar datos de la facultad")
    opc = int(input("Ingrese opcion"))
    while opc != 3:
        if opc == 1:
            numero=int(input("Ingrese codigo de facultad"))
            lista.opcion1(numero)
        elif opc ==2:
            nombre=input("Ingrese nombre carrera")
            lista.opcion2(nombre)
            