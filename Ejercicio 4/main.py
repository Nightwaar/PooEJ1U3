from clasecontratado import contratado
from claseexterno import externo
from claseplanta import planta
from claseempleado import empleados
from manejadorempleados import manejador
if __name__=="__main__":
    mane=manejador()
    mane.cargar()
    print("""
1.Registrar horas
2.Total de tarea
3.Ayuda economica
4.Calcular sueldo""")
    opc=int(input("Ingrese opcion"))
    while opc<5:
        match opc:
            case 1:
                dni=input("Ingrese el dni")
                horas=input("Ingrese la cantidad de horas a incrementar")
                manejador.accion1(dni,horas)
            case 2:
                print("?")
            case 3:
                manejador.accion3()
            case 4:
                manejador.accion4()